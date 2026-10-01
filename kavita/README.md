# Home Assistant Add-on: Kavita

Kavita is a self-hosted digital library and reading server for comics, manga,
and books. It includes browser-based readers, multi-user access, OPDS support,
reading lists, collections, and device integrations.

Kavita is self-contained and uses an embedded SQLite database. This add-on does
not install or require PostgreSQL, MariaDB, or another database add-on.

## Installation

1. Add this repository to the Home Assistant add-on store:
   [![Add repository on my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ftomjansen%2Fhassio-addons)
1. Install `Kavita`.
1. Start the add-on and open its web UI.
1. Create the administrator account, then add one or more libraries from
   `/share` or `/media`.

## Storage

| Kavita path | Home Assistant location | Purpose |
| --- | --- | --- |
| `/kavita/config` | Add-on configuration storage | SQLite database, settings, covers, cache, logs, and backups |
| `/share` | Home Assistant shared storage | Book, comic, and manga libraries |
| `/media` | Home Assistant media storage | Book, comic, and manga libraries |

Kavita's configuration and database are included in add-on backups. Library
files under `/share` and `/media` must be backed up separately.

The add-on has read-write access to both library locations because Kavita can
manage covers, bookmarks, and other library-related files. Use Home Assistant
storage permissions and Kavita user permissions to limit access as needed.

## Configuration

Kavita is configured through its web interface. The server listens on port
`5000`; Home Assistant controls the host port mapping.

## Source

- Add-on repository: https://github.com/tomjansen/hassio-addons
- Upstream project: https://github.com/Kareadita/Kavita
- Upstream documentation: https://wiki.kavitareader.com/
- Base image: `ghcr.io/kareadita/kavita:0.9.1`
