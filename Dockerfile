FROM python:3.10.8

ENV FLASK_APP=lab1 

COPY ./requirements.txt /requirements.txt

RUN python3 -m pip install -r /requirements.txt

COPY ./lab1 /lab1

WORKDIR /Back_End_Lab1

CMD flask run --host 0.0.0.0 -p 5000