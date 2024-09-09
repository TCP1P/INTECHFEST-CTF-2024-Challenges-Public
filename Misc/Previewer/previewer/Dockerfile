FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y xvfb libxcb-cursor0 libglib2.0-0 libsm6 libxrender1 libxext6 python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install flask pyqt5 --break-system-packages

COPY ./src /app/src/

RUN mkdir -p /app/src/static/results
RUN chmod +x /app/src/entrypoint.sh
RUN chmod 777 /app/src/static/results

COPY flag.txt /flag.txt
RUN chmod 644 /flag.txt
RUN chown root:root /flag.txt
RUN mv /flag.txt /flag-`cat /proc/sys/kernel/random/uuid`.txt

RUN useradd -m ctf
WORKDIR /home/ctf

USER ctf
ENTRYPOINT ["/app/src/entrypoint.sh"]
