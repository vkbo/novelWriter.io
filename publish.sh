#!/bin/bash

make html
rsync -avPh --delete build/html/ novelwriter.io:www/
