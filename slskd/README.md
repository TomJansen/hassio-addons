# Home Assistant Add-on: slskd

slskd is a modern, web-based client for the Soulseek file-sharing network. It
supports searching, downloading, sharing, chat, and API-based integrations.

## Installation

1. Add this repository to the Home Assistant add-on store:
   [![Add repository on my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ftomjansen%2Fhassio-addons)
1. Install `slskd`.
1. Enter your Soulseek username and password in the add-on options, then start
   the add-on.
1. Open the web UI and immediately change the default `slskd`/`slskd` web
   credentials.

## Storage

| slskd path | Home Assistant location | Purpose |
| --- | --- | --- |
| `/config` | Add-on configuration storage | Configuration, database, logs, and certificates |
| `/share/slskd/downloads` | `/share` | Default completed download directory |
| `/share/slskd/incomplete` | `/share` | Default incomplete download directory |
| `/share` | Home Assistant shared storage | Optional download or shared folders |
| `/media` | Home Assistant media storage | Optional download or shared folders |

Application state under `/config` is included in add-on backups. Files under
`/share` and `/media` must be backed up separately.

## Configuration

| Option | Default | Description |
| --- | --- | --- |
| `PUID` | `1000` | User ID slskd uses for file ownership. |
| `PGID` | `1000` | Group ID slskd uses for file ownership. |
| `TZ` | `UTC` | Time zone, for example `Europe/Copenhagen`. |
| `UMASK` | `0022` | Permission mask used when slskd creates files. |
| `REMOTE_CONFIGURATION` | `true` | Allow configuration through the web UI. |
| `REMOTE_FILE_MANAGEMENT` | `false` | Allow files to be deleted through the API and web UI. |
| `SLSK_USERNAME` | empty | Soulseek network username. |
| `SLSK_PASSWORD` | empty | Soulseek network password (masked in the add-on options). |
| `DOWNLOADS_DIR` | `/share/slskd/downloads` | Completed download directory. |
| `INCOMPLETE_DIR` | `/share/slskd/incomplete` | Incomplete download directory. |
| `SHARED_DIRS` | empty | Semicolon-separated directories to share, such as `/media/music;/share/books`. |

Sharing is disabled by default. Only add directories whose contents you intend
to make available to other Soulseek users. You can configure shares and most
other settings in the web UI while `REMOTE_CONFIGURATION` is enabled.

The Soulseek credentials are separate from the web UI login. Leave the add-on
fields empty to keep credentials configured in slskd's web UI or `slskd.yml`.
slskd's YAML configuration takes precedence over environment variables, so
credentials already saved in `slskd.yml` may need to be removed there before
changes to these add-on options take effect. Changing Soulseek credentials
requires resetting the Soulseek connection.

The web interface is available over HTTP on port `5030` and HTTPS with a
self-signed certificate on port `5031`. Soulseek listens for incoming TCP
connections on port `50300`. For the best peer-to-peer connectivity, forward
TCP port `50300` from your router to the Home Assistant host and ensure the
add-on's host port remains `50300`.

Do not expose the web ports to the internet with their default credentials.
Remote configuration allows authenticated administrators to view and change
settings that may contain secrets.

## Source

- Add-on repository: https://github.com/tomjansen/hassio-addons
- Upstream project: https://github.com/slskd/slskd
- Upstream documentation: https://github.com/slskd/slskd/tree/master/docs
- Base image: `ghcr.io/slskd/slskd:0.26.0`
