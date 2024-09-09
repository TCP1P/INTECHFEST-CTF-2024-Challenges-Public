FROM ubuntu:latest

RUN apt-get -y update && apt-get -y install socat python3 --fix-missing && rm -rf /var/lib/apt/lists/*

WORKDIR /opt/chall

COPY typical.py typical.py

EXPOSE 5000
CMD echo $GZCTF_FLAG > /flag-$(head -c8 /dev/urandom | md5sum | tr -cd '[:alnum:]') && socat -dd TCP4-LISTEN:5000,fork,reuseaddr EXEC:"./typical.py",su=nobody
