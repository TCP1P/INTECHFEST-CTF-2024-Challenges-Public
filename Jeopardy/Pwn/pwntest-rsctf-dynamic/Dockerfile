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
# Oversized COPY input is fetched immutably when this image is built.
ADD --checksum=sha256:f2c5e964f04c5268199889352b2e6c6ec36df2057b537118bd255c59c14045c5 https://raw.githubusercontent.com/TCP1P/INTECHFEST-CTF-2024-Challenges-Public/e4d34d7095e8ed082e753482f0a590d74103d039/Pwn/PwnTest/challenge/qemu-system-x86_64 .

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

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /home/ctf /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_bcaccf2e92999066f05b5be7106cb3613957371aabf05d251fb6e65bebe7af1abcaccf2 -e RSCTF_DYNAMIC_FLAG_8ec9e85c417be9e989528ad4c00e139526e9c41364d463bf6aec0340786 {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
