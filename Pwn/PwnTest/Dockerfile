FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install -y xinetd libpixman-1-dev libepoxy-dev libspice-server-dev libfdt-dev libusb-1.0-0-dev libasound-dev libaio-dev libslirp-dev
RUN groupadd -r ctf && useradd -r -g ctf ctf

# privesc
RUN setcap cap_setuid+ep /usr/bin/python3.10

WORKDIR /home/ctf

COPY challenge/bzImage .
COPY challenge/rootfs.cpio.gz .
COPY challenge/run.sh .
COPY challenge/bios .
COPY challenge/qemu-system-x86_64 .

RUN echo '#!/bin/bash\nservice xinetd restart && /bin/sleep infinity' > /etc/init.sh
RUN echo 'service ctf\n\
{\n\
    disable = no\n\
    socket_type = stream\n\
    protocol = tcp\n\
    wait = no\n\
    user = ctf\n\
    type = UNLISTED\n\
    port = 9006\n\
    bind = 0.0.0.0\n\
    server = /home/ctf/run.sh\n\
}' > /etc/xinetd.d/ctf

# REAL FLAG
COPY challenge/flag.txt /root

RUN chmod 400 /etc/xinetd.d/ctf
RUN chmod 444 /home/ctf/*
RUN chmod 550 /home/ctf/run.sh /etc/init.sh /home/ctf/qemu-system-x86_64
RUN chmod 1733 /tmp /var/tmp /dev/shm
RUN chown -R root:ctf /home/ctf

RUN service xinetd restart
