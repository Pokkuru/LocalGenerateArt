FROM python:3.8-slim AS builder
WORKDIR /app

COPY ./requirements.txt  .
COPY ./LocalGenerateNFT  .
RUN apt update -y && apt upgrade -y
RUN apt install -y libpq-dev gcc
RUN pip install -r requirements.txt