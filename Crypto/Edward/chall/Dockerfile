FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y nano socat gcc
RUN pip install ed25519

WORKDIR /opt

COPY challenge.py .


CMD echo $GZCTF_FLAG > flag.txt && socat TCP-LISTEN:5000,fork,reuseaddr EXEC:'python3 challenge.py'
