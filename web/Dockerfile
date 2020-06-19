FROM python:3
USER root
RUN apt-get apt-utils
RUN apt-get update && apt-get install -y lsb-release
RUN apt-get update && apt-get install -y python3-pip
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
WORKDIR /usr/src/app/appLIS_flask_SpamDetect
CMD [ "python3", "app.py" ]

