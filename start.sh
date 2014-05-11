#!/bin/bash

for f in `ls ./BMFonts/$1/*.jsn`
do
  echo "Processing $f file..."
  ./bmfb.py "$f"
done
