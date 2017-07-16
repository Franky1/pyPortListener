FROM python:3.5-slim
MAINTAINER Arvid Teichtmann

RUN apt-get update && apt-get -y upgrade

RUN pip install -U requests

ADD pyPortListener.py /

EXPOSE 5055

CMD [ "python", "./pyPortListener.py" ]
