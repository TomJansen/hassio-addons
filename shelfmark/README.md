# Home Assistant Add-on: Shelfmark

Shelfmark is a self-hosted interface for searching and requesting books and
audiobooks from configurable web, torrent, Usenet, and IRC sources.

## Installation

1. Add this repository to the Home Assistant add-on store:
   [![Add repository on my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ftomjansen%2Fhassio-addons)
1. Install `Shelfmark`.
1. Configure and start the add-on.
1. Open the web UI and configure the sources and download clients you use.

## Storage

| Shelfmark path | Home Assistant location | Purpose |
| --- | --- | --- |
| `/config` | Add-on configuration storage | Settings, database, and artwork cache |
| `/share/cwa-book-ingest` | `/share` | Default destination for downloaded books |
| `/share` | Home Assistant shared storage | Other selectable download destinations |
| `/media` | Home Assistant media storage | Other selectable download destinations |

The default destination is shared with the Calibre-Web Automated add-on, so
completed books can be imported automatically. Shelfmark creates the directory
when it starts. Change `INGEST_DIR` if you use a different library application
or storage layout.

Torrent and Usenet clients must see completed downloads at the same path that
Shelfmark uses. Choose a path under `/share` or `/media` that is available to
both add-ons.

## Configuration

| Option | Default | Description |
| --- | --- | --- |
| `PUID` | `1000` | User ID Shelfmark uses for file ownership. |
| `PGID` | `1000` | Group ID Shelfmark uses for file ownership. |
| `TZ` | `UTC` | Time zone, for example `Europe/Copenhagen`. |
| `INGEST_DIR` | `/share/cwa-book-ingest` | Default book download destination, shared with CWA. |
| `SEARCH_MODE` | `universal` | Use `universal` metadata search or query sources with `direct`. |

Most source, authentication, notification, and download-client settings are
configured in Shelfmark's web interface. The standard image includes Chromium
for browser-assisted downloads and should have at least 2 GB of available RAM
when that feature is used.

The web server listens on port `8084`; Home Assistant controls the host port
mapping. Shelfmark exposes `/api/health`, which is used by the add-on watchdog.

## Source

- Add-on repository: https://github.com/tomjansen/hassio-addons
- Upstream project: https://github.com/calibrain/shelfmark
- Upstream image: `ghcr.io/calibrain/shelfmark:v1.3.14`
