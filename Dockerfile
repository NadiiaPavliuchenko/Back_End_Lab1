FROM python:3.10.8

ENV FLASK_APP=npavlbackendlab1

COPY ./requirements.txt /requirements.txt

RUN python3 -m pip install -r /requirements.txt

COPY ./npavlbackendlab1 /npavlbackendlab1

WORKDIR /

CMD flask run --host 0.0.0.0 -p 5000