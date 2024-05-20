# How to run/edit?
## Development Environment
Install VSCode and open the *flask* folder. Follow the tutorial at https://code.visualstudio.com/docs/python/tutorial-flask.
The Python version that was used during development was 3.11.3

## Production Environment
Create a new Ubuntu server.

1. Install Docker (if not already installed) by following the tutorial here: https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository

2. Clone the GitHub repo to the server

3. Edit the .env file and change DOMAIN_NAME to your domain name.

4. Determine if you want to run the server in unencrypted mode (HTTP) or encrypted mode (HTTPS), then, follow the corresponding set of instructions below.

### Unencrypted HTTP


### Encrypted HTTPS
1. Open the compose.yaml file and uncomment line 9 so that the NGINX server can operate in unencrypted mode. This is necessary to setup Certbot, 
    and will be disabled later.

2. Navigate to the GitHub repo folder and run the following command in your terminal to build the docker images `sudo docker compose build`

3. Run the following command in your terminal to setup your SSL certificates. Follow the instructions provided by Certbot.
    You will need to provide your domain name(s) and your email address.
    `sudo docker compose run certbot certbot certonly --webroot`

4. Open the compose.yaml file and comment out line 9 - then, uncomment line 7, so that the NGINX server can operate in encrypted mode.

5. While in the compose.yaml file, uncomment line 58 so that the certbot service can automatically handle certificate renewals.

6. Build and run the webserver by executing the following command while inside the GitHub repo folder: `sudo docker compose up -d --build`

7. When you're ready, stop the webserver by executing the following command while inside the GitHub repo folder: `sudo docker compose down`

Use docker-compose starting with this template: https://github.com/docker/awesome-compose/tree/master/nginx-wsgi-flask