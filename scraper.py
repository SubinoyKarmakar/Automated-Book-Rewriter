import requests
from bs4 import BeautifulSoup

# Fetch and extract the main chapter content (headings and paragraphs) from the given URL.
def fetch_chapter_text(url):    # Send HTTP request to the URL
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')      # Parse the HTML content using BeautifulSoup

    content_div = soup.find('div', {'class': 'mw-parser-output'})       # Locate the main content area in the page
    if not content_div:
        return "Content not found"  # Return message if main content is missing

    texts = []      # Extract all paragraphs and headings (h2, h3)
    for tag in content_div.find_all(['p', 'h2', 'h3']):
        text = tag.get_text(strip=True)
        if text:    # Skip empty tags
            texts.append(text)

    return "\n\n".join(texts)       # Join all extracted text blocks with double line breaks

