#!/bin/zsh -l
# shellcheck shell=bash

set -e
cd "$(dirname "$0")"

BIN_DIR="./.bin"
FFMPEG_URL="https://evermeet.cx/ffmpeg/getrelease/zip"

if [ ! -f "$BIN_DIR/ffmpeg" ]; then
	mkdir -p "$BIN_DIR"
	cd "$BIN_DIR"

	curl -L "$FFMPEG_URL" -o "./ffmpeg.zip"
	unzip "./ffmpeg.zip"
	rm "./ffmpeg.zip"

	/usr/sbin/softwareupdate --install-rosetta --agree-to-license

	arch -x86_64 ./ffmpeg &>/dev/null || true
	xattr -d com.apple.quarantine ./ffmpeg || true
	arch -x86_64 ./ffmpeg || true
fi
