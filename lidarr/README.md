# Home Assistant Add-on: Lidarr Nightly

Lidarr nightly is a music collection manager for Usenet and BitTorrent users, packaged as a Home Assistant add-on.

This add-on uses the LinuxServer.io nightly Lidarr image.

## Installation

1. Add this repository to the Home Assistant add-on store:
   [![Add repository on my Home Assistant](https://my.home-assistant.io/badges/supervisor_add_addon_repository.svg)](https://my.home-assistant.io/redirect/supervisor_add_addon_repository/?repository_url=https%3A%2F%2Fgithub.com%2Ftomjansen%2Fhassio-addons)
1. Install `Lidarr nightly`.
1. Save your add-on configuration.
1. Start the add-on.
1. Open the web UI and finish configuring Lidarr.

## Configuration

Web UI access is available at `http://homeassistant:8686` or through the Home Assistant sidebar when ingress is enabled.

### Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `PGID` | int | `0` | Group ID for file permissions |
| `PUID` | int | `0` | User ID for file permissions |
| `TZ` | str | | Timezone, for example `Europe/London` |
| `localdisks` | str | | Local drives to mount, for example `sda1,sdb1` |
| `networkdisks` | str | | SMB shares to mount, for example `//SERVER/SHARE` |
| `cifsusername` | str | | SMB username for network shares |
| `cifspassword` | str | | SMB password for network shares |
| `cifsdomain` | str | | SMB domain for network shares |
| `env_vars` | list | `[]` | Extra environment variables passed to the container |

### Example

```yaml
PGID: 0
PUID: 0
TZ: "Europe/Copenhagen"
localdisks: "sda1,sdb1"
networkdisks: "//192.168.1.100/downloads,//nas.local/music"
cifsusername: "mediauser"
cifspassword: "password123"
cifsdomain: "workgroup"
env_vars: []
```

## Source

- Add-on repository: https://github.com/tomjansen/hassio-addons
- Upstream image: https://github.com/linuxserver/docker-lidarr
