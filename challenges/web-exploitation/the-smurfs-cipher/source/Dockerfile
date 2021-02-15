FROM php:7.4.13-apache

RUN apt update; \
    apt -y upgrade

COPY flag.txt /flag.txt
COPY password.txt /password.txt
COPY public_html/ /var/www/html/
