#!/bin/sh
set -eu
: "${GZCTF_FLAG:?GZCTF_FLAG is required}"
printf '%s\n' "$GZCTF_FLAG" > /root/flag.txt
unset GZCTF_FLAG
chmod 400 /root/flag.txt

su - deno -c '
  while true; do
    deno task start
  done
'
