"# Login_template"

# This this a simple docker container that using vue.js as front end and python as back end to save and displat data when log in

1. Presiquit: Docker and Docker Compose
2. Open terminal, move to the folder contain Dockerfile and docker-compose
3. Run docker-compose up on terminal, this will create the container to run this server, the first time may take a few time
4. After the docker complete, you can access the login page by access http://localhost/ for login page or http://localhost:12345/users to get all users data

#h3 notice:
when running on server, you need to go to the index.html file and changing the localhost to your corresponding private ipv4 address. You can access to this server by this ip address as long as you and your server are in the same LAN or your server have public ip address.
