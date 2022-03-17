FROM python:3.9-buster

COPY . /PiMotionDetector
WORKDIR /PiMotionDetector

RUN apt update
RUN apt -y install nano python3-setuptools python3-dev python3-rpi.gpio

RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt -v

CMD python3 main.py