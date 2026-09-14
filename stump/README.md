# Home Assistant Add-on: Stump

Stump is a self-hosted, multi-user server for comics, manga, and digital books.
It provides browser-based readers, OPDS catalogs, Kobo and KOReader sync, and
support for EPUB, PDF, CBZ/ZIP, and CBR/RAR files.

Stump is self-contained and uses an embedded SQLite database. It does not
require MariaDB or another database add-on.

## Installation

1. Add this repository to the Home Assistant add-on store:
   [![Add repository on my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ftomjansen%2Fhassio-addons)
1. Install `Stump`.
1. Configure and start the add-on.
1. Open the web UI, create the initial account, and add a library using
   `/share/stump/books`.

## Storage

| Stump path | Home Assistant location | Purpose |
| --- | --- | --- |
| `/config` | Add-on configuration storage | SQLite database, settings, and generated assets |
| `/share/stump/books` | `/share` | Default library shared with Shelfmark |
| `/share` | Home Assistant shared storage | Other selectable library locations |
| `/media` | Home Assistant media storage | Other selectable library locations |

Stump reads books in place and does not require an ingest or import database.
Add `/share/stump/books` as a Stump library, then configure its scanning
schedule according to how frequently new downloads arrive.

The SQLite database and configuration are included with add-on backups. Books
stored under `/share` or `/media` must be backed up separately.

## Configuration

| Option | Default | Description |
| --- | --- | --- |
| `PUID` | `1000` | User ID Stump uses for file ownership. |
| `PGID` | `1000` | Group ID Stump uses for file ownership. |
| `TZ` | `UTC` | Time zone, for example `Europe/Copenhagen`. |
| `ENV_VARS` | empty | Additional environment variables passed to Stump. |

Enter `NAME=value` assignments separated by semicolons in the single `ENV_VARS`
text box. Do not use newlines or spaces around the semicolons:

```yaml
ENV_VARS: "ENABLE_KOBO_SYNC=true;STUMP_VERBOSITY=2"
```

Values may contain spaces, but cannot contain semicolons.

`PUID`, `PGID`, `TZ`, `PATH`, `LD_PRELOAD`, `LD_LIBRARY_PATH`,
`STUMP_CONFIG_DIR`, `STUMP_CLIENT_DIR`, `STUMP_PORT`, `STUMP_IN_DOCKER`, and
`PDFIUM_PATH` are managed by the add-on and cannot be overridden through
`ENV_VARS`.

The web server listens on port `10801`; Home Assistant controls the host port
mapping.

Stump is beta software until it reaches version 1.0. Back up its configuration
before upgrading and review upstream release notes for migration warnings.

## Source

- Add-on repository: https://github.com/tomjansen/hassio-addons
- Upstream project: https://github.com/stumpapp/stump
- Upstream documentation: https://www.stumpapp.dev/docs/getting-started/installation/docker
- Base image: `docker.io/aaronleopold/stump:0.1.7`
