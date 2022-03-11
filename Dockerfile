# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
ADD script.py health.py /
RUN pip3 install paho-mqtt &&\
    apt-get update && apt-get install -y iputils-ping procps
HEALTHCHECK --interval=12s --timeout=12s --start-period=30s \  
	CMD python /health.py
CMD [ "python", "./script.py" ]