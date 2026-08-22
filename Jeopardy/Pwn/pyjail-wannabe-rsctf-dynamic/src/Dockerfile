# check=skip=JSONArgsRecommended
FROM ubuntu:22.04
RUN apt update && apt install socat python3 python3-pip gdb -y

WORKDIR /app
COPY chall.py /app/chall.py
COPY flag.txt /flag.txt

RUN chmod 755 /app/chall.py
RUN chmod 444 /flag.txt

EXPOSE 9000

CMD socat TCP-LISTEN:9000,reuseaddr,fork exec:/app/chall.py

# RSCTF dynamic-flag compatibility layer. The build-time scan records
# exact marker-bearing files; runtime replacement is therefore bounded
# to those files instead of walking the image on every team start.
USER root
COPY rsctf-entrypoint.sh /usr/local/bin/rsctf-entrypoint
RUN set -eu; \
    chmod 0555 /usr/local/bin/rsctf-entrypoint; \
    : > /etc/rsctf-flag-targets; \
    for root in /app/chall.py /app /src /srv /home /opt /var/www /challenge /chall /ctf /root /usr/src /usr/local/bin /workspace /flag /flag.txt; do \
      if [ -e "$root" ]; then \
        find "$root" -xdev -type f ! -path /usr/local/bin/rsctf-entrypoint -exec grep -lF -e RSCTF_DYNAMIC_FLAG_19416a3980d101fc547140a7c200e73a91779cbd8a0b276 -e RSCTF_DYNAMIC_FLAG_a65c9e983fe06316a53c6198f5f88135124 {} + >> /etc/rsctf-flag-targets 2>/dev/null || true; \
      fi; \
    done; \
    sort -u /etc/rsctf-flag-targets > /etc/rsctf-flag-targets.sorted; \
    mv /etc/rsctf-flag-targets.sorted /etc/rsctf-flag-targets; \
    while IFS= read -r target; do [ -f "$target" ] && chmod a+w "$target"; done < /etc/rsctf-flag-targets
ENTRYPOINT ["/usr/local/bin/rsctf-entrypoint"]
