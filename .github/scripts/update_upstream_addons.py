#!/usr/bin/env python3
"""Update pinned upstream add-on images from their latest GitHub releases."""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path


SEMVER = re.compile(r"^[vV]?(\d+)\.(\d+)\.(\d+)$")


@dataclass(frozen=True)
class Addon:
    directory: str
    repository: str
    image: str


ADDONS = (
    Addon(
        directory="calibre-web-automated",
        repository="crocodilestick/Calibre-Web-Automated",
        image="crocodilestick/calibre-web-automated",
    ),
    Addon(
        directory="shelfmark",
        repository="calibrain/shelfmark",
        image="ghcr.io/calibrain/shelfmark",
    ),
)


def version_tuple(tag: str) -> tuple[int, int, int]:
    match = SEMVER.fullmatch(tag.strip())
    if not match:
        raise ValueError(f"Expected a stable vMAJOR.MINOR.PATCH tag, got {tag!r}")
    return tuple(int(part) for part in match.groups())


def latest_release(repository: str, token: str | None) -> str:
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repository}/releases/latest",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "hassio-addons-updater",
            "X-GitHub-Api-Version": "2022-11-28",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except (urllib.error.URLError, TimeoutError) as error:
        raise RuntimeError(f"Could not query the latest {repository} release: {error}") from error

    tag = payload.get("tag_name", "")
    version_tuple(tag)
    return tag


def image_platforms(reference: str) -> set[str]:
    try:
        result = subprocess.run(
            ["docker", "buildx", "imagetools", "inspect", "--raw", reference],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as error:
        detail = error.stderr.strip() or error.stdout.strip() or f"exit code {error.returncode}"
        raise RuntimeError(f"Could not inspect {reference}: {detail}") from error

    manifest = json.loads(result.stdout)
    return {
        f"linux/{platform['architecture']}"
        for item in manifest.get("manifests", [])
        if (platform := item.get("platform", {})).get("os") == "linux"
        and platform.get("architecture")
    }


def current_tag(build: dict, addon: Addon) -> str:
    references = set(build.get("build_from", {}).values())
    if not references:
        raise ValueError(f"{addon.directory}/build.json has no build_from images")
    if len(references) != 1:
        raise ValueError(f"{addon.directory}/build.json architectures do not use one version")

    reference = references.pop()
    prefix = f"{addon.image}:"
    if not reference.startswith(prefix):
        raise ValueError(f"Expected {reference!r} to start with {prefix!r}")
    tag = reference.removeprefix(prefix)
    version_tuple(tag)
    return tag


def bump_addon_version(config_path: Path) -> tuple[str, str]:
    source = config_path.read_text()
    pattern = re.compile(r'^(version:\s*)["\']?(\d+)\.(\d+)\.(\d+)["\']?\s*$', re.MULTILINE)
    match = pattern.search(source)
    if not match:
        raise ValueError(f"Could not find a semantic version in {config_path}")

    old = ".".join(match.group(index) for index in range(2, 5))
    new = f"{match.group(2)}.{match.group(3)}.{int(match.group(4)) + 1}"
    updated = pattern.sub(lambda found: f'{found.group(1)}"{new}"', source, count=1)
    config_path.write_text(updated)
    return old, new


def write_outputs(changes: list[str], warnings: list[str]) -> None:
    summary = ["## Upstream add-on update check", ""]
    summary.extend(changes or ["No newer compatible upstream releases were found."])
    if warnings:
        summary.extend(["", "### Skipped", "", *warnings])
    summary_text = "\n".join(summary) + "\n"

    if summary_path := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary_path, "a", encoding="utf-8") as stream:
            stream.write(summary_text)
    else:
        print(summary_text, end="")

    if output_path := os.environ.get("GITHUB_OUTPUT"):
        with open(output_path, "a", encoding="utf-8") as stream:
            stream.write(f"updated={'true' if changes else 'false'}\n")
            stream.write("summary<<UPDATER_SUMMARY\n")
            stream.write(summary_text)
            stream.write("UPDATER_SUMMARY\n")


def parse_release_overrides(values: list[str]) -> dict[str, str]:
    overrides: dict[str, str] = {}
    for value in values:
        directory, separator, tag = value.partition("=")
        if not separator:
            raise ValueError(f"Invalid --release value {value!r}; expected ADDON=TAG")
        version_tuple(tag)
        overrides[directory] = tag
    return overrides


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--release", action="append", default=[], metavar="ADDON=TAG")
    parser.add_argument("--no-verify-images", action="store_true")
    args = parser.parse_args()

    overrides = parse_release_overrides(args.release)
    known = {addon.directory for addon in ADDONS}
    unknown = set(overrides) - known
    if unknown:
        raise ValueError(f"Unknown add-on release override(s): {', '.join(sorted(unknown))}")

    changes: list[str] = []
    warnings: list[str] = []
    token = os.environ.get("GITHUB_TOKEN")

    for addon in ADDONS:
        build_path = args.root / addon.directory / "build.json"
        config_path = args.root / addon.directory / "config.yaml"
        build = json.loads(build_path.read_text())
        installed = current_tag(build, addon)
        available = overrides.get(addon.directory) or latest_release(addon.repository, token)

        if version_tuple(available) <= version_tuple(installed):
            continue

        reference = f"{addon.image}:{available}"
        if not args.no_verify_images:
            try:
                platforms = image_platforms(reference)
            except (RuntimeError, json.JSONDecodeError) as error:
                warnings.append(f"- `{addon.directory}` `{available}`: {error}")
                continue
            missing = {"linux/amd64", "linux/arm64"} - platforms
            if missing:
                warnings.append(
                    f"- `{addon.directory}` `{available}`: `{reference}` is missing "
                    + ", ".join(f"`{platform}`" for platform in sorted(missing))
                )
                continue

        for architecture in build["build_from"]:
            build["build_from"][architecture] = reference
        build_path.write_text(json.dumps(build, indent=2) + "\n")
        old_addon, new_addon = bump_addon_version(config_path)
        changes.append(
            f"- `{addon.directory}`: upstream `{installed}` → `{available}`; "
            f"add-on `{old_addon}` → `{new_addon}`"
        )

    write_outputs(changes, warnings)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError) as error:
        print(f"::error::{error}", file=sys.stderr)
        raise SystemExit(1) from error
