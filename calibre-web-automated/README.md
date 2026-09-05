# Home Assistant Add-on: Calibre-Web Automated

Calibre-Web Automated (CWA) provides a web interface for a Calibre library,
plus automatic ingest, conversion, and metadata workflows.

## Installation

1. Add this repository to the Home Assistant add-on store:
   [![Add repository on my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ftomjansen%2Fhassio-addons)
1. Install `Calibre-Web Automated`.
1. Configure and start the add-on.
1. Open the web UI.

## Storage

The add-on uses Home Assistant-managed locations rather than arbitrary host
paths:

| CWA path | Home Assistant location | Purpose |
| --- | --- | --- |
| `/config` | Add-on configuration storage | CWA settings, backups, and Calibre configuration |
| `INGEST_DIR` (`/share/cwa-book-ingest`) | `/share` or `/media` | Put books here for automatic ingestion |
| `/share/calibre-web-automated/library` | `/share` | Default Calibre library location |
| `/share/calibre-web-automated/plugins` | `/share` | Optional Calibre plugins |

The configured ingest directory and the two CWA `/share` directories are
created when the add-on starts. In the CWA setup screen, select
`/share/calibre-web-automated/library` as the library. The ingest directory can
be any subdirectory below `/share` or `/media`.

CWA removes source files after successfully importing them. Always use a
dedicated ingest directory, never an existing library or general books folder.
To connect Shelfmark, give both add-ons the same `INGEST_DIR` value.

## Configuration

| Option | Default | Description |
| --- | --- | --- |
| `PUID` | `1000` | User ID CWA uses for file ownership. |
| `PGID` | `1000` | Group ID CWA uses for file ownership. |
| `TZ` | `UTC` | Time zone, for example `Europe/Copenhagen`. |
| `INGEST_DIR` | `/share/cwa-book-ingest` | Dedicated ingest directory shared with download tools such as Shelfmark. |
| `HARDCOVER_TOKEN` | empty | Optional Hardcover metadata-provider API token. |
| `NETWORK_SHARE_MODE` | `false` | Enable when the configuration or library is on NFS/SMB storage. |

`NETWORK_SHARE_MODE` disables SQLite WAL and uses polling-based file watching,
which avoids common locking and event-notification issues with network shares.

The web server always listens on port `8083`; Home Assistant controls the host
port mapping.

## Source

- Add-on repository: https://github.com/tomjansen/hassio-addons
- Upstream project: https://github.com/crocodilestick/Calibre-Web-Automated
- Upstream image: `crocodilestick/calibre-web-automated:v4.0.6`
