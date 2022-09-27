FROM python:latest
ADD ./* /reading_server/
WORKDIR /reading_server
EXPOSE 8080
CMD python3 /reading_server/server.py 8080
