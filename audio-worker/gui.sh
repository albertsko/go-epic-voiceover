#!/bin/zsh -l
# shellcheck shell=bash

set -e
cd "$(dirname "$0")"
source .venv/bin/activate

cd ACE-Step
acestep --port 7865 --bf16 false --torch_compile true --cpu_offload true --overlapped_decode true
