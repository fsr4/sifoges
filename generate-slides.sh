#!/usr/bin/env sh

set -e

if [ $# -ne 1 ]; then
  echo 'Usage: ./generate-slides.sh <top-file>'
  exit
fi

chmod +x ./generate-tex.py

./generate-tex.py $1

temp_dir=.tmp-xetex

mkdir $temp_dir
xelatex -file-line-error -interaction=nonstopmode -synctex=1 -output-directory=$temp_dir main.tex
xelatex -file-line-error -interaction=nonstopmode -synctex=1 -output-directory=$temp_dir main.tex

mv $temp_dir/main.pdf ./main.pdf
rm -r $temp_dir
rm main.tex
