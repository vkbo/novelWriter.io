#!/bin/bash

make clean html
rsync -avPh --delete build/html/ novelwriter.io:www/
