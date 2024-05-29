#!/bin/bash
# Replace all environment variables in default.conf
envsubst '$FLASK_SERVER_ADDR,$GOACCESS_SERVER_ADDR,$DOMAIN_NAME,$GOACCESS_DOMAIN_NAME,$GOACCESS_ADMIN_IP_ADDRESS' < /tmp/default.conf > /etc/nginx/conf.d/default.conf

#if [ ! -f /etc/letsencrypt/live/$DOMAIN_NAME/fullchain.pem ]; then \
#    certbot certonly --standalone --non-interactive --agree-tos --email $EMAIL --preferred-challenges http --domains $DOMAIN_NAME,www.$DOMAIN_NAME\
#    && echo "Installed certificates for first time";\
#fi

#chmod 644 /etc/letsencrypt/live/$DOMAIN_NAME/fullchain.pem
#chmod 644 /etc/letsencrypt/live/$DOMAIN_NAME/privkey.pem

nginx -g 'daemon off;'

#sleep infinity