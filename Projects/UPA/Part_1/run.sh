#!/bin/bash

source Part_1/bin/activate

cd Part_1/

python3 URL_Fetcher.py > url_test.txt

head -n 10 url_test.txt | python3 scraper.py