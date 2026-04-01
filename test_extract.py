import urllib.request
import re

url = 'https://usethenews.ch/bild-der-woche/bild-der-woche-13-sek-il-ulmen-fernandes-fall-digitale-gewalt/'
html = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read().decode('utf-8')

# Find the main content div
content_match = re.search(r'<div[^>]*class=["\'][^"\']*entry-content[^"\']*["\'][^>]*>(.*?)</div>\s*<(?:div|footer|aside)', html, re.DOTALL | re.IGNORECASE)
if not content_match:
    # try wp-block-post-content
    content_match = re.search(r'<div[^>]*class=["\'][^"\']*wp-block-post-content[^"\']*["\'][^>]*>(.*?)</div>\s*<(?:div|footer|aside)', html, re.DOTALL | re.IGNORECASE)

if content_match:
    content = content_match.group(1)
    paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', content, re.DOTALL | re.IGNORECASE)
    texts = []
    for p in paragraphs:
        text = re.sub(r'<[^>]+>', '', p).strip()
        if text: texts.append(text)
    print("Found paragraphs:", len(texts))
    for t in texts: print("-", t)
else:
    print("No content div found. Trying global paragraph search.")
    paragraphs = re.findall(r'<p[^>]*>(.*?)</p>', html, re.DOTALL | re.IGNORECASE)
    # Filter out short or navigation paragraphs
    texts = []
    for p in paragraphs:
        text = re.sub(r'<[^>]+>', '', p).strip()
        if len(text) > 50:
            texts.append(text)
    print("Found global paragraphs:", len(texts))
    for t in texts: print("-", t)
