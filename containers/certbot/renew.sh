#certbot certonly -n -d $DOMAIN_NAME -d www.$DOMAIN_NAME
certbot renew

# Keep the container alive for a day before letting it die and restart
sleep 86400