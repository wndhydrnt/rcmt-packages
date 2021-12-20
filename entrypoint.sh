#!/usr/bin/env bash

set -euo pipefail

pip install -qq poetry
rcmt run --config /opt/work/rcmt.yaml --packages /opt/work/packages /opt/work/run.py
