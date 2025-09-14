#!/bin/zsh -l
# shellcheck shell=bash

set -e
cd "$(dirname "$0")"

if ! command -v pyenv &>/dev/null; then
	brew install pyenv
fi

if ! grep -q 'eval "$(pyenv init --path)"' ~/.zshrc; then
	echo 'eval "$(pyenv init --path)"' >>~/.zshrc
	source "$HOME/.zshrc"
fi

pyenv install --skip-existing 3.11
pyenv local 3.11

[ -d ".venv" ] || python -m venv .venv
source .venv/bin/activate

printf '\n\e[1m%s\e[0m\n' "Installing chatterbox-tts..."
pip install --upgrade pip setuptools wheel cython
pip install numpy
pip install pkuseg==0.0.25
pip install chatterbox-tts
