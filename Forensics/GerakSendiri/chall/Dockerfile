FROM ubuntu:22.04

RUN apt-get update && \
    apt-get -y install python3 \
    socat

RUN     useradd ctf
WORKDIR /home/ctf

COPY main.py      /home/ctf/

RUN chown -R root:root  /home/ctf
RUN chmod -R 555        /home/ctf

EXPOSE 6980
ENTRYPOINT ["socat", "TCP-LISTEN:6980,reuseaddr,fork,nodelay,su=ctf", "EXEC:'python3 main.py'"]