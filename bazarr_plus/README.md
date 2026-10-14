# Home Assistant Add-on: Bazarr+

Bazarr+ finds, synchronizes, and translates subtitles for movies, TV shows,
and sports. It can work as a standalone subtitle search application or connect
to Sonarr, Radarr, and Sportarr to automate an entire media library.

## Installation

1. Add this repository to the Home Assistant add-on store:
   [![Add repository on my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ftomjansen%2Fhassio-addons)
1. Install `Bazarr+`.
1. Configure and start the add-on.
1. Open the web UI and complete the setup wizard.

Sonarr, Radarr, and Sportarr are optional. Choose the standalone Discover mode
in the setup wizard to search for subtitles without connecting a media library.

## Storage

| Bazarr+ path | Home Assistant location | Purpose |
| --- | --- | --- |
| `/config` | Add-on configuration storage | Database, settings, plugins, backups, and logs |
| `/share` | Home Assistant shared storage | Optional movie, TV, and sports libraries |
| `/media` | Home Assistant media storage | Optional movie, TV, and sports libraries |

Configuration under `/config` is included in add-on backups. Media and
subtitle files under `/share` and `/media` must be backed up separately.

Bazarr+ must see each connected library through the same path used by its
source application. If the paths differ, configure path mappings for the
Sonarr, Radarr, or Sportarr instance under **Settings > Connections**. For
example, map a Sonarr path to `/media/tv` when that is where the same library
is mounted in this add-on.

## Configuration

| Option | Default | Description |
| --- | --- | --- |
| `PUID` | `0` | User ID Bazarr+ uses for file ownership. |
| `PGID` | `0` | Group ID Bazarr+ uses for file ownership. |
| `TZ` | `UTC` | Time zone, for example `Europe/Copenhagen`. |
| `UMASK` | `002` | Permission mask applied to files Bazarr+ creates. |

The defaults run Bazarr+ with root ownership so it can write subtitles to Home
Assistant shared storage. Set `PUID` and `PGID` to a less privileged account
when the ownership and permissions of every configured media directory allow
that account to write files.

Configure library sources, media servers, subtitle providers, languages,
authentication, and optional AI translation in the web interface. When a
connected application runs in another add-on, use the Home Assistant host
address rather than `localhost`; each add-on has its own network namespace.

The web server listens on port `6767`; Home Assistant controls the host port
mapping. Do not expose the port to the internet without enabling Bazarr+
authentication or placing it behind an authenticated reverse proxy.

## Migrating from Bazarr

Back up the existing Bazarr `/config` directory before using it with Bazarr+.
Bazarr+ automatically migrates compatible settings and data, but its changes
are not fully backwards-compatible. Restoring the pre-migration backup is the
safest way to return to upstream Bazarr.

## Source

- Add-on repository: https://github.com/tomjansen/hassio-addons
- Bazarr+ project: https://github.com/LavX/bazarr
- Bazarr+ documentation: https://lavx.github.io/bazarr/
- Getting started: https://lavx.github.io/bazarr/guides/getting-started.html
- Base image: `ghcr.io/lavx/bazarr:2.7.1`
