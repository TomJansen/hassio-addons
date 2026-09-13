ARG BUILD_FROM=docker.io/aaronleopold/stump:0.1.5
FROM ${BUILD_FROM}

LABEL \
    org.opencontainers.image.source="https://github.com/tomjansen/hassio-addons" \
    org.opencontainers.image.description="Home Assistant add-on for Stump"

COPY --chmod=0755 addon-init /addon-init

ENTRYPOINT ["/addon-init"]
