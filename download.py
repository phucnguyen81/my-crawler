import requests
from bs4 import BeautifulSoup
import time
import random
from urllib.parse import urljoin


print("Hello from my-crawler!")

# Function to download the page with retry logic and exponential backoff
def download_page(url, retries=3, backoff=2):
    for attempt in range(retries):
        try:
            headers = {
                'Host': 'readfrom.net',
                'User-Agent': 'curl/8.7.1',
                'Accept': '*/*',
            }
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Error downloading the page {url}, attempt {attempt + 1}/{retries}, error {e}")
            if attempt < retries - 1:
                time.sleep(backoff * (2 ** attempt))  # Exponential backoff
            else:
                print(f"Failed to download page after {retries} attempts.")
                return None

# Function to find the next page link from the current page's HTML structure
def get_next_page_link(soup, base_url):
    next_page_span = soup.find('span', {'class': 'page_next'})

    if next_page_span:
        next_page_link = next_page_span.find('a')
        if next_page_link and 'href' in next_page_link.attrs:
            return urljoin(base_url, next_page_link['href'])  # Ensure the next page URL is absolute
        else:
            print("Next page link found but it doesn't contain 'href'.")
    else:
        print("Next page link not found.")
    return None

# Main crawler function with polite crawling and edge case handling
def crawl_website(start_url):
    url = start_url
    page_number = 1

    while url:
        print(f"Downloading page {page_number}: {url}")

        # Download the page
        page_html = download_page(url)
        if page_html is None:
            print(f"Stopping crawler. Failed to download page {page_number}.")
            break  # Stop if the page couldn't be downloaded

        # Parse the HTML content
        soup = BeautifulSoup(page_html, 'html.parser')

        # Save the page content locally (optional)
        with open(f"page_{page_number}.html", "w", encoding="utf-8") as f:
            f.write(page_html)

        # Find the next page link
        next_page_url = get_next_page_link(soup, url)

        # If there's a next page, update the URL, else break the loop
        if next_page_url:
            url = next_page_url
        else:
            print(f"No more pages found after page {page_number}.")
            break

        page_number += 1

        # Polite crawling: add a randomized delay to avoid overwhelming the server
        delay = 1 + random.uniform(0.5, 1.5)
        print(f"Sleeping for {delay:.2f} seconds before next request...")
        time.sleep(delay)

# Starting URL
start_url = "https://readfrom.net/iain-hollingshead/page,1,237593-beta_male.html"

# Run the crawler
crawl_website(start_url)
