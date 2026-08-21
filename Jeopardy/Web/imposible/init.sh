#!/bin/sh
set -eu
: "${RSCTF_FLAG:?RSCTF_FLAG is required}"
export FLAG="$RSCTF_FLAG"
unset RSCTF_FLAG
exec ./main
