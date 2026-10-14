ARG BUILD_FROM=ghcr.io/lavx/bazarr:2.7.1
FROM ${BUILD_FROM}

LABEL \
    org.opencontainers.image.source="https://github.com/tomjansen/hassio-addons" \
    org.opencontainers.image.description="Home Assistant add-on for Bazarr+"

COPY --chmod=0755 addon-init /addon-init

ENTRYPOINT ["/addon-init"]
CMD ["python", "docker/supervisor.py", "--no-update", "--config", "/config"]
