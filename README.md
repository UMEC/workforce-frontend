# Workforce Project API And Frontend

## Documentation For Frontend And Backend

1. [Frontend](/frontend/README.md)
1. [Backend](/backend/README.md)

## Deploying The Whole Application In Production

We use docker to deploy in production. The specific container that we extend is 
[here](https://github.com/tiangolo/uwsgi-nginx-flask-docker) and the tag is `python3.8`.
The container is set up to use uwsgi and nginx to host a flask app and has been extended
to also serve the static frontend.

To build and run the containers, do the following:

```
# Assemble necessary backend resources
cd backend
pipenv install
pipenv run pip freeze > requirements.txt
cd ..

# Assemble necessary frontend resources
cd frontend
npm install
npm run build
cd ..

# Build the docker container and start it
docker build --no-cache -t workforce .
docker stop workforce_container
docker rm workforce_container
docker run -d --name workforce_container -p 80:80 workforce
```

The container redirects the nginx error logs to stderr and stdout, not to a file, so you 
can attach to the container to debug. However, if you want to poke around the file system
you can with the following command:

```
docker exec -it workforce_container bash
```
