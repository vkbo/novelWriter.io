#!/bin/bash

rm -rf build/*
uv run sphinx-build -W -b html source build/html
rsync -avPh --delete build/html/ novelwriter.io:www/
