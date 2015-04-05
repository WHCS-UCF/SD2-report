#!/bin/sh
if [ ! -e "$1" ]; then
  echo "PDF to convert to image required"
  exit 1
fi

BASE=`basename --suffix=".pdf" "$1"`

convert  -density 200 "$1" -alpha off "${BASE}.png"
echo "$1 -> ${BASE}.png"
