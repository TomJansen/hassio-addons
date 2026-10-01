ARG BUILD_FROM=ghcr.io/kareadita/kavita:0.9.1
FROM ${BUILD_FROM}

LABEL \
    org.opencontainers.image.source="https://github.com/tomjansen/hassio-addons" \
    org.opencontainers.image.description="Home Assistant add-on for Kavita"

# Persist Kavita's SQLite database and configuration in add-on storage.
RUN rm -rf /kavita/config && ln -s /config /kavita/config
