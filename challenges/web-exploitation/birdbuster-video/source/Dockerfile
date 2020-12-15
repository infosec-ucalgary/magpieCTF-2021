FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

RUN apk update; \
    apk upgrade; \
    apk add sqlite zbar

RUN apk add build-base python3-dev jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

COPY ./app /app

RUN pip3 install -r requirements.txt

# Initialize database
RUN /usr/bin/sqlite3 database.db -init populate.sql
