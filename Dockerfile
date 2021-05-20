FROM python:3.8-alpine as main

RUN apk update

RUN apk -U add \
    ca-certificates \
    cargo \
    chromium \ 
    chromium-chromedriver \ 
    curl \
    g++ \
    gcc \
    git \
    libc-dev \ 
    libffi-dev \
    libressl-dev \
    libxml2-dev \
    libxslt-dev \
    linux-headers \ 
    make \
    musl-dev \
    openssl \
    openssl-dev 

RUN update-ca-certificates

RUN pip3 install \
    twisted \
    Scrapy==2.3.0

RUN pip3 install \
    git+https://github.com/scanfactory/scrapy-selenium-seleniumwire

COPY ./spider.py /spider.py

RUN ls -l //usr/bin/chromedriver
ENTRYPOINT python3 /spider.py