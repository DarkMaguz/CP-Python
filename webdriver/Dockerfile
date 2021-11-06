FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y nano bzip2 wget libxt6 libdbus-glib-1-2 libx11-xcb1 libgtk-3-0 --no-install-recommends

RUN mkdir /opt/app
COPY requirements.txt /opt/app/
RUN pip3 install -r /opt/app/requirements.txt

COPY main.py /opt/app/

#RUN useradd -ms /bin/bash mage
#RUN chown mage:mage /opt/app
#USER mage

WORKDIR /opt/app/
