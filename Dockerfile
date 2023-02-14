# syntax=docker/dockerfile:1

FROM python:3.9.16-buster

WORKDIR C:/Users/user/Desktop/Drowsiness

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY . .


CMD [ "python3", "main.py", "flask", "run", "--host=0.0.0.0"]