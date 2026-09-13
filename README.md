# Home Assistant Add-ons

This repository contains Home Assistant add-ons:

## Add-ons Provided

- [Lidarr nightly](lidarr/) - Music collection manager for Usenet and BitTorrent users.
- [Stump](stump/) - Comics, manga, and digital book server with OPDS support.
- [Shelfmark](shelfmark/) - Search and request books and audiobooks from multiple sources.

## Lidarr

Lidarr can monitor RSS feeds for new albums from your favorite artists and interface with download clients and indexers to grab, sort, and rename releases.

See the [Lidarr add-on README](lidarr/README.md) for configuration, options, and usage details.

## Stump

Stump manages comics, manga, and digital books with browser-based readers,
multi-user access, OPDS catalogs, and device sync. It uses an embedded SQLite
database and does not require a separate database add-on.

See the [Stump add-on README](stump/README.md) for configuration and storage
setup.

## Shelfmark

Shelfmark searches configured sources for books and audiobooks and can send
completed book downloads to Stump's library folder.

See the [Shelfmark add-on README](shelfmark/README.md) for configuration and
storage setup.
