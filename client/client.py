import requests
import json

def print_sitemap(sitemap, depth=0):
    for page, links in sitemap.items():
        print("  " * depth + f"- {page}")
        print_sitemap(links, depth + 1)

if __name__ == '__main__':
    server_url = 'http://localhost:5000/crawl'
    target_url = input("Enter the URL to crawl: ")
    
    response = requests.post(server_url, json={"url": target_url})
    
    if response.status_code == 200:
        sitemap = response.json()
        print("Sitemap:")
        print_sitemap(sitemap)
    else:
        print(f"Error: {response.json()}")
