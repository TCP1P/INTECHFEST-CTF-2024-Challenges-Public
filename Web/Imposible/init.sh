#!/bin/sh
set -eu
: "${GZCTF_FLAG:?GZCTF_FLAG is required}"
export FLAG="$GZCTF_FLAG"
unset GZCTF_FLAG
exec ./main
