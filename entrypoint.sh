#!/usr/bin/env bash

set -euo pipefail

pip install -qq poetry
poetry install
/opt/entrypoint.sh run --config /opt/work/rcmt.yaml --packages /opt/work/packages /opt/work/run.py
