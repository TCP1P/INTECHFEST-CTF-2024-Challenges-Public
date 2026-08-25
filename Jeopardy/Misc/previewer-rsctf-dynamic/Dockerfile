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
# Original final-stage ENTRYPOINT is wrapped by RSCTF at runtime.

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /app/src /home/ctf /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_f6a9a9e8122e776f1dda20c81091e5f165447f297f57310ba29757cea6b7eb7ff6a9a9e -e RSCTF_DYNAMIC_FLAG_c9efe3116f25cf75fe9c20ec6a434a8ecfe5b24e6149284814ba0a919c1 {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    find / -xdev -maxdepth 1 -type f -exec grep -lF -e RSCTF_DYNAMIC_FLAG_f6a9a9e8122e776f1dda20c81091e5f165447f297f57310ba29757cea6b7eb7ff6a9a9e -e RSCTF_DYNAMIC_FLAG_c9efe3116f25cf75fe9c20ec6a434a8ecfe5b24e6149284814ba0a919c1 {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do \
      [ -f "$target" ] || continue; \
      chmod a+w "$target"; \
      parent=$(dirname "$target"); \
      while [ "$parent" != / ]; do chmod a+x "$parent"; parent=$(dirname "$parent"); done; \
    done < /etc/rsctf-flag-targets
USER ctf
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint", "/app/src/entrypoint.sh"]
