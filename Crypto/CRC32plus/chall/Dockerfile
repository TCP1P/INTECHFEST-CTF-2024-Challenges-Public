FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y nano socat
RUN pip install pycryptodome

WORKDIR /opt

COPY server.py .

CMD test -n "$GZCTF_FLAG" && printf '%s\n' "$GZCTF_FLAG" > flag.txt && unset GZCTF_FLAG && exec socat TCP-LISTEN:5000,fork,reuseaddr EXEC:'python3 server.py'
