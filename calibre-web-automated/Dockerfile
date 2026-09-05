ARG BUILD_FROM
FROM ${BUILD_FROM}

LABEL \
    org.opencontainers.image.source="https://github.com/tomjansen/hassio-addons" \
    org.opencontainers.image.description="Home Assistant add-on for Calibre-Web Automated"

# The upstream image does not include jq. It is used only to translate the
# Supervisor-managed add-on options into the environment CWA expects.
RUN apt-get update \
    && apt-get install -y --no-install-recommends jq \
    && rm -rf /var/lib/apt/lists/*

COPY addon-init /addon-init
RUN chmod 0755 /addon-init

ENTRYPOINT ["/addon-init"]
