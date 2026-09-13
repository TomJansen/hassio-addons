ARG BUILD_FROM=docker.io/aaronleopold/stump:0.1.5
FROM ghcr.io/jqlang/jq:1.8.1 AS jq
FROM ${BUILD_FROM}

LABEL \
    org.opencontainers.image.source="https://github.com/tomjansen/hassio-addons" \
    org.opencontainers.image.description="Home Assistant add-on for Stump"

COPY --from=jq /jq /usr/local/bin/jq
COPY --chmod=0755 addon-init /addon-init

ENTRYPOINT ["/addon-init"]
