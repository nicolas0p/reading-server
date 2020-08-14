# Number Reading Server

## Description
This project's goal is to create an HTTP server able to receive an integer between -99999 and 99999 and reply the number written in full in a json dict format.

## Executing

This project is dockerized, to build the project's docker image, use the following command:
```
docker build -t reading_server_image .
```
To execute the reading server inside the docker container, use:
```
docker run -it --name reading_server -p 8080:8080 reading_server
```
