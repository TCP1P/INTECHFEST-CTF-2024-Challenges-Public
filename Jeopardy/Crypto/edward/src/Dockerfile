# check=skip=JSONArgsRecommended
FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y nano socat gcc
RUN pip install ed25519

WORKDIR /opt

COPY challenge.py .


CMD test -n "$RSCTF_FLAG" && printf '%s\n' "$RSCTF_FLAG" > flag.txt && unset RSCTF_FLAG && exec socat TCP-LISTEN:5000,fork,reuseaddr EXEC:'python3 challenge.py'
