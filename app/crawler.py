import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def crawl_domain(base_url, visited=None):
    if visited is None:
        visited = set()
    
    sitemap = {}
    domain = urlparse(base_url).netloc
    
    try:
        response = requests.get(base_url)
        if response.status_code != 200:
            return sitemap
        
        soup = BeautifulSoup(response.text, 'html.parser')
        links = set()
        
        for link in soup.find_all('a', href=True):
            full_url = urljoin(base_url, link['href'])
            if urlparse(full_url).netloc == domain and full_url not in visited:
                links.add(full_url)
        
        visited.add(base_url)
        sitemap[base_url] = {}
        for link in links:
            sitemap[base_url][link] = crawl_domain(link, visited)
        
    except Exception as e:
        print(f"Error crawling {base_url}: {e}")
    
    return sitemap
