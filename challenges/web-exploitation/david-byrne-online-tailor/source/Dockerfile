FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine 

COPY ./app /app 
COPY ./flag /flag 

RUN pip3 install -r requirements.txt