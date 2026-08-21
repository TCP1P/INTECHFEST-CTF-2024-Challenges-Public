#!/bin/sh
set -eu

: "${RSCTF_FLAG:?RSCTF_FLAG is required}"
umask 022
printf '%s\n' "$RSCTF_FLAG" > /flag.txt
chmod 0444 /flag.txt
unset RSCTF_FLAG

exec socat TCP-LISTEN:6980,reuseaddr,fork,nodelay,su=ctf "EXEC:python3 main.py"
