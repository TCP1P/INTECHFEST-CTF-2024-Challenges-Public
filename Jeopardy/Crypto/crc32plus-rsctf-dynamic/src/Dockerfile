# check=skip=JSONArgsRecommended
FROM python:3.11-slim

RUN apt-get update
RUN apt-get install -y nano socat
RUN pip install pycryptodome

WORKDIR /opt

COPY server.py .

CMD test -n "$RSCTF_FLAG" && printf '%s\n' "$RSCTF_FLAG" > flag.txt && unset RSCTF_FLAG && exec socat TCP-LISTEN:5000,fork,reuseaddr EXEC:'python3 server.py'
