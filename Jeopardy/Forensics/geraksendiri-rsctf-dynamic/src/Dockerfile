FROM ubuntu:22.04

RUN apt-get update && \
    apt-get -y install python3 \
    socat

RUN     useradd ctf
WORKDIR /home/ctf

COPY main.py      /home/ctf/
COPY start.sh     /usr/local/bin/start-challenge

RUN chown -R root:root  /home/ctf
RUN chmod -R 555        /home/ctf
RUN chmod 0555 /usr/local/bin/start-challenge

EXPOSE 6980
ENTRYPOINT ["/usr/local/bin/start-challenge"]
