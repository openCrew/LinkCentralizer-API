FROM python:3.7-alpine

WORKDIR /flaskr/database

COPY src/requirements.txt ./

RUN pip install -r requirements.txt

CMD [ "python", "db.py" ]