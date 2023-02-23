# syntax=docker/dockerfile:1

FROM python:3.9.16-buster@sha256:0cf9e69897d5bae4ca29eeee2aab2e6612d9f2d021f1ca892cf0740f7806938c

WORKDIR C:/Users/user/Desktop/Drowsiness

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . .


CMD [ "python3", "main.py", "flask", "run", "--host=0.0.0.0"]