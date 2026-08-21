FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y nano socat gcc
RUN pip install ed25519

WORKDIR /opt

COPY challenge.py .


CMD test -n "$GZCTF_FLAG" && printf '%s\n' "$GZCTF_FLAG" > flag.txt && unset GZCTF_FLAG && exec socat TCP-LISTEN:5000,fork,reuseaddr EXEC:'python3 challenge.py'
