FROM python:3.5-slim
MAINTAINER Arvid Teichtmann

RUN apt-get update && apt-get -y upgrade

RUN pip install -U websockets && \
    pip install -U geocoder && \
    pip install -U requests && \
    pip install -U netifaces

ADD pyCanWebsocketServer.py /
ADD pyJsonBlob.py /

EXPOSE 8080

CMD [ "python", "./pyCanWebsocketServer.py" ]
