import urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

base_url = "https://www.otomoto.pl/osobowe?search%5Border%5D=relevance_web" 

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

    links = [a["href"] for a in soup.find_all("a", href=re.compile("oferta"))]
    full_links = [urljoin(base_url, link) for link in links]

    return full_links

def main():
    urls = [base_url]   
    visited = set()     
    results = [] 

    max_pages = 120

    while urls and len(visited) < max_pages:
        current = urls.pop(0)  
        if current in visited:
            continue

        print("Visiting:", current)
        visited.add(current)

        new_links = go_to_site(current)
        for link in new_links:
            if link not in visited and link not in urls:
                urls.append(link)
                results.append(link)

    with open("urls.txt", "w", encoding="utf-8") as f:
        for item in results:
            f.write(item + "\n")

if __name__ == "__main__":
    main()
