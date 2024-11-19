import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import argparse

def download_image(url, path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        filename = os.path.join(path, url.split('/')[-1])
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def scrape_images(url, depth, path, visited):
    # Print the current state of the parameters for debugging
    print(f"\n=== scrape_images called ===")
    print(f"URL: {url}")
    print(f"Depth: {depth}")
    print(f"Path: {path}")
    print(f"Visited: {list(visited)}")  # Convert to list for readable output``
    if depth < 0 or url in visited:
        return
    print(f"Visiting URL: {url} (Depth: {depth})")
    visited.add(url)
    try:
        base_domain = urlparse(url).netloc
        print(f"\nProcessing URL: {url} (Depth: {depth})")
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        for img_tag in soup.find_all('img'):
            img_url = urljoin(url, img_tag.get('src'))
            if img_url.endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                print(f"Downloading image: {img_url}")
                download_image(img_url, path)
        for link_tag in soup.find_all('a'):
            link_url = urljoin(url, link_tag.get('href'))
            if base_domain == urlparse(link_url).netloc:
                print(f"Found new link: {link_url}")
                # Only follow internal links
                if link_url not in visited:
                     print(f"Found internal link: {link_url}")
                     scrape_images(link_url, depth - 1, path, visited)
                else:
                     print(f"Found external link: {link_url}")
            
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", action="store_true", help="Enable recursive scraping")
    parser.add_argument("-l", type=int, default=5, help="Set depth level for recursion")
    parser.add_argument("-p", type=str, default="./data/", help="Set path to save images")
    parser.add_argument("url", type=str, help="URL to scrape")
    args = parser.parse_args()
    
    if not os.path.exists(args.p):
        os.makedirs(args.p)
    
    visited = set()
    scrape_images(args.url, args.l if args.r else 0, args.p, visited)

if __name__ == "__main__":
    main()
