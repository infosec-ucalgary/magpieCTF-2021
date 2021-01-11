FROM alpine:3.12

RUN apk update
RUN apk add python3 socat

COPY server.py /home/

EXPOSE 20000

CMD socat TCP-LISTEN:20000,fork,reuseaddr EXEC:"python3 /home/server.py"
