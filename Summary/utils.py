import requests
from bs4 import BeautifulSoup

def fetch_webpage(url):
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def parse_webpage(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No title found'
    paragraphs = [p.get_text(strip=True) for p in soup.find_all('p')]
    
    return title, paragraphs
