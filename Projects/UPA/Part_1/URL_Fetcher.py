import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def go_to_site(url):
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
    products = [a["href"] for a in soup.find_all("a", attrs=re.compile("product--title"))]
    
    return products



def main():
    base_url = "https://www.kindermaxx.de/en/toys/open-ended-play"
    page_count = 7 # how many to load (when i tested it 7 was maximum)
    all_products = []
    for i in range(page_count):
        final_url = base_url+f"?p={i+1}"
        all_products += go_to_site(final_url)

    for product_link in all_products:
        print(product_link)

if __name__ == "__main__":
    main()
