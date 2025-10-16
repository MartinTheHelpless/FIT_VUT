#!/bin/bash

source Part_1/bin/activate

python3 fetcher.py > url_test.txt

head -n 10 url_test.txt | python3 scraper.py