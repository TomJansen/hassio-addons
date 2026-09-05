ARG BUILD_FROM=ghcr.io/calibrain/shelfmark:v1.3.14
FROM ${BUILD_FROM}

LABEL \
    org.opencontainers.image.source="https://github.com/tomjansen/hassio-addons" \
    org.opencontainers.image.description="Home Assistant add-on for Shelfmark"

COPY --chmod=0755 addon-init /addon-init

# Keep the upstream dumb-init entrypoint and insert the add-on configuration
# wrapper before Shelfmark's own startup script.
CMD ["/addon-init"]
