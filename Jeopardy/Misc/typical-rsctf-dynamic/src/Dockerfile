# check=skip=JSONArgsRecommended
FROM ubuntu:latest

RUN apt-get -y update && apt-get -y install socat python3 --fix-missing && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/chall

COPY typical.py typical.py

EXPOSE 5000
CMD test -n "$RSCTF_FLAG" && printf '%s\n' "$RSCTF_FLAG" > /flag-$(head -c8 /dev/urandom | md5sum | cut -c1-16) && unset RSCTF_FLAG && exec socat -dd TCP4-LISTEN:5000,fork,reuseaddr EXEC:"./typical.py",su=nobody
