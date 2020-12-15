FROM alpine:3.12

#Openresty
RUN wget 'http://openresty.org/package/admin@openresty.com-5ea678a6.rsa.pub'
RUN mv 'admin@openresty.com-5ea678a6.rsa.pub' /etc/apk/keys/
RUN . /etc/os-release
RUN echo "http://openresty.org/package/alpine/v3.12/main" | tee -a /etc/apk/repositories
RUN apk update
RUN apk add openresty

# Configure nginx
COPY config/nginx.conf /usr/local/openresty/nginx/conf/nginx.conf
COPY config/proxy.conf /usr/local/openresty/nginx/sites/proxy.conf


# Expose the port nginx is reachable on
EXPOSE 8080
EXPOSE 1337

# Let supervisord start nginx & php-fpm
ENTRYPOINT openresty -g 'daemon off;'

# Configure a healthcheck to validate that everything is up&running
HEALTHCHECK --timeout=10s CMD curl --silent --fail http://127.0.0.1:8080/
