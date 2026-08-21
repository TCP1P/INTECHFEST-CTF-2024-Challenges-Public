#!/bin/sh
set -eu
: "${RSCTF_FLAG:?RSCTF_FLAG is required}"
printf '%s\n' "$RSCTF_FLAG" > /root/flag.txt
unset RSCTF_FLAG
chmod 400 /root/flag.txt

su - deno -c '
  while true; do
    deno task start
  done
'
