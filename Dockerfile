FROM python:3.10.8

ENV FLASK_APP=npavlbackendlab1
ENV FLASK_DEBUG=$FLASK_DEBUG

COPY ./requirements.txt /requirements.txt

RUN python -m pip install -r /requirements.txt

COPY ./npavlbackendlab1 /npavlbackendlab1

WORKDIR /

CMD flask run --host 0.0.0.0 -p $PORT