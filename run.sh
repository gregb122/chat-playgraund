#!/bin/sh

set -o errexit
set -o nounset

uvicorn main:app --host "0.0.0.0" --port $PORT --reload --ws 'auto' \
--loop 'auto' --worke


exec "$@"