
FROM python:3.7

RUN mkdir -p /flask_app/

WORKDIR /flask_app/

ADD app.py .
ADD setup.py .

RUN python3.7 setup.py install

#ARG FLASK_PORT

ENTRYPOINT flask run -h 0.0.0.0 -p 5000 --with-threads