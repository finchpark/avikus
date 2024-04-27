FROM python:3.10

COPY . /src
WORKDIR /src

#RUN apt-get update && apt-get install -y sqlite3
RUN pip install -r requirements.txt