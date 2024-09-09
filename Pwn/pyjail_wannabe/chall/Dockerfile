FROM ubuntu:22.04
RUN apt update && apt install socat python3 python3-pip gdb -y

WORKDIR /app
COPY chall.py /app/chall.py
COPY flag.txt /flag.txt

RUN chmod 755 /app/chall.py
RUN chmod 444 /flag.txt

EXPOSE 9000

CMD socat TCP-LISTEN:9000,reuseaddr,fork exec:/app/chall.py
