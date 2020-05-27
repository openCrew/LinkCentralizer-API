FROM python:3

WORKDIR /flaskr
COPY requirements.txt /flaskr/requirements.txt
RUN pip3 install -r requirements.txt
CMD flask run --host=0.0.0.0
