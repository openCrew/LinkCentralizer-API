FROM python:3.7-alpine

WORKDIR /flaskr
COPY requirements.txt /flaskr/requirements.txt
RUN pip3 install -r requirements.txt
CMD gunicorn  --bind 0.0.0.0:5000 --log-level warning  --reload  wsgi:application


EXPOSE 5000