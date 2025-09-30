#!/bin/bash

source Part_1/bin/activate

python3 Part_1/URL_Fetcher.py > url_test.txt

head -n 10 Part_1/url_test.txt | python3 Part_1/scraper.py