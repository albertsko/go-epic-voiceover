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

pyenv install --skip-existing 3.10
pyenv local 3.10

[ -d "venv" ] || python -m venv venv
source venv/bin/activate

printf '\n\e[1m%s\e[0m\n' "Upgrading pip..."
pip install --upgrade pip

printf '\n\e[1m%s\e[0m\n' "Installing ace-step..."
git clone https://github.com/ace-step/ACE-Step.git || true
cd ACE-Step
rm -rf .git

pip install -e .
