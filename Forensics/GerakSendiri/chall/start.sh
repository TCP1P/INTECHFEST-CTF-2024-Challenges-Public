#!/bin/sh
set -eu

: "${GZCTF_FLAG:?GZCTF_FLAG is required}"
umask 022
printf '%s\n' "$GZCTF_FLAG" > /flag.txt
chmod 0444 /flag.txt
unset GZCTF_FLAG

exec socat TCP-LISTEN:6980,reuseaddr,fork,nodelay,su=ctf "EXEC:python3 main.py"
