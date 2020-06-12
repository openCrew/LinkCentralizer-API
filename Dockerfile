FROM python:3.7.4-alpine

WORKDIR /flaskr

RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt /flaskr/requirements.txt
RUN pip install -r requirements.txt
#CMD gunicorn  --bind 0.0.0.0:5000   --reload --log-level debug --workers=3 \
#    wsgi:application


EXPOSE 5000
