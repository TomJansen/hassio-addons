ARG BUILD_FROM=lscr.io/linuxserver/bazarr:version-v1.6.2
FROM ${BUILD_FROM}

LABEL \
    org.opencontainers.image.source="https://github.com/tomjansen/hassio-addons" \
    org.opencontainers.image.description="Home Assistant add-on for Bazarr"

COPY --chmod=0755 addon-init /addon-init

ENTRYPOINT ["/addon-init"]
