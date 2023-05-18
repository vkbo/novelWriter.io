#!/bin/bash

make html
rsync -avPh --delete build/html/ novelwriter.io:www/
rsync -avPh source/_fixed/ novelwriter.io:www/
