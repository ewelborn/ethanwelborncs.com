FROM certbot/certbot

# Add bash for boot cmd
RUN apk add bash

# Add bash file to container
COPY --chown=nginx:nginx renew.sh renew.sh

ENTRYPOINT []