FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y nano socat
RUN pip install pycryptodome

WORKDIR /opt

COPY server.py .

CMD echo $GZCTF_FLAG > flag.txt && socat TCP-LISTEN:5000,fork,reuseaddr EXEC:'python3 server.py'
