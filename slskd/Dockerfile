ARG BUILD_FROM=ghcr.io/slskd/slskd:0.26.0
FROM ${BUILD_FROM}

LABEL \
    org.opencontainers.image.source="https://github.com/tomjansen/hassio-addons" \
    org.opencontainers.image.description="Home Assistant add-on for slskd"

COPY --chmod=0755 addon-init /addon-init

ENTRYPOINT ["/usr/bin/tini", "--", "/addon-init"]
CMD ["./slskd"]
