# pull official base image
FROM python:3.10
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# set work directory
WORKDIR /usr/src/finance

COPY ./requirements.txt /usr/src/finance/requirements.txt
# install dependencies
RUN pip install -r /usr/src/finance/requirements.txt

COPY . /usr/src/finance
