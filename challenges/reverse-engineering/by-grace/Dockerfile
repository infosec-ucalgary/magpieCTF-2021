FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine

# update, upgrade, last line needed for Pillow to install properly
RUN apk update; \
    apk upgrade; \
    apk add \
    freetype-dev \
    fribidi-dev \
    harfbuzz-dev \
    jpeg-dev \
    lcms2-dev \
    openjpeg-dev \
    tcl-dev \
    tiff-dev \
    tk-dev \
    zlib-dev \
    gcc \
    musl-dev

# Copy the app and cronAdd script
COPY ./app /app
COPY cronAdd .

# Add the cron job to the crontab
RUN (crontab -l 2> /dev/null; echo "*/15 * * * * /app/scrub.sh")| crontab -

# append the cronAdd to the supervisord.ini file to allow cron to start
RUN cat cronAdd >> /etc/supervisor.d/supervisord.ini

# make scrub.sh executable
RUN chmod +x /app/scrub.sh

# install all the requirements for flask
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

