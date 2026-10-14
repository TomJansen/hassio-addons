# Home Assistant Add-on: Bazarr

Bazarr is a companion application for Sonarr and Radarr. It monitors movies
and TV episodes, then searches for and downloads subtitles according to your
language profiles and provider settings.

## Installation

1. Add this repository to the Home Assistant add-on store:
   [![Add repository on my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ftomjansen%2Fhassio-addons)
1. Install `Bazarr`.
1. Configure and start the add-on.
1. Open the web UI and complete Bazarr's setup.

Bazarr requires an existing Sonarr or Radarr installation. It does not download
video files itself.

## Storage

| Bazarr path | Home Assistant location | Purpose |
| --- | --- | --- |
| `/config` | Add-on configuration storage | Database, settings, backups, and logs |
| `/share` | Home Assistant shared storage | Movie and TV libraries |
| `/media` | Home Assistant media storage | Movie and TV libraries |

Configuration under `/config` is included in add-on backups. Media and
subtitle files under `/share` and `/media` must be backed up separately.

Bazarr must see each library through the same path that Sonarr or Radarr uses.
If their paths differ, configure Bazarr path mappings under **Settings > Sonarr**
or **Settings > Radarr**. For example, map a Sonarr path to `/media/tv` when
that is where the same library is mounted in this add-on.

## Configuration

| Option | Default | Description |
| --- | --- | --- |
| `PUID` | `0` | User ID Bazarr uses for file ownership. |
| `PGID` | `0` | Group ID Bazarr uses for file ownership. |
| `TZ` | `UTC` | Time zone, for example `Europe/Copenhagen`. |
| `UMASK` | `002` | Permission mask applied to files Bazarr creates. |

The defaults run Bazarr with root ownership so it can write subtitles to Home
Assistant shared storage. Set `PUID` and `PGID` to a less privileged account
when the ownership and permissions of every configured media directory allow
that account to write files.

Configure Sonarr, Radarr, subtitle providers, languages, and authentication in
Bazarr's web interface. When Sonarr or Radarr runs in another add-on, use the
Home Assistant host address rather than `localhost`; each add-on has its own
network namespace.

The web server listens on port `6767`; Home Assistant controls the host port
mapping. Do not expose the port to the internet without enabling Bazarr
authentication or placing it behind an authenticated reverse proxy.

## Source

- Add-on repository: https://github.com/tomjansen/hassio-addons
- Upstream project: https://github.com/morpheus65535/bazarr
- Upstream documentation: https://wiki.bazarr.media/
- Container documentation: https://docs.linuxserver.io/images/docker-bazarr/
- Base image: `lscr.io/linuxserver/bazarr:version-v1.6.2`
