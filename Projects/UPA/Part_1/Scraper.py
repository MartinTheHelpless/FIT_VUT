import sys
import urllib.request
from bs4 import BeautifulSoup
import re

def get_product_info(url):
    """Function description"""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
    }
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req) as response:
            html = response.read().decode("utf-8", errors="ignore")
    except Exception as e:
        print("Failed:", url, e)
        return []

    soup = BeautifulSoup(html, "html.parser")
    product_name = soup.find("h1", attrs=re.compile("product--title")).text
    product_price = soup.find("span", attrs=re.compile("price--content content--default")).text
    
    info_value = [td.text for td in soup.find_all("td", attrs=re.compile("product--properties-value"))]
    info_value.insert(0, product_price) # add price to start
    info_value.insert(0, product_name)
    info_value.insert(0, url)
    return info_value

def main():
    for line in sys.stdin:
        info = get_product_info(line)
        for i in info:
            print(i.strip(), end='\t')
if __name__ == "__main__":
    main()