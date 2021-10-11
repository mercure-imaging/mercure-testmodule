#!/usr/bin/env bash
set -Eeo pipefail
echo "-- Starting testmodule..."
python testmodule.py $MERCURE_IN_DIR $MERCURE_OUT_DIR
echo "-- Done."
