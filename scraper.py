import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def scrape_quotes():
    print("Starting web scraping of quotes.toscrape.com...")
    all_quotes = []
    
    for page in range(1, 11):
        url = f"https://quotes.toscrape.com/page/{page}/"
        print(f"Scraping Page {page}...")
        
        try:
            response = requests.get(url, timeout=15)
            response.raise_for_status()
        except Exception as e:
            print(f"Error fetching page {page}: {e}")
            continue
            
        soup = BeautifulSoup(response.content, "html.parser")
        quotes = soup.select(".quote")
        
        for quote in quotes:
            text = quote.select_one(".text").get_text(strip=True)
            author = quote.select_one(".author").get_text(strip=True)
            tags = [tag.get_text(strip=True) for tag in quote.select(".tags .tag")]
            
            all_quotes.append({
                "Page": page,
                "Quote": text,
                "Author": author,
                "Tags": ", ".join(tags)
            })
        
        # Respectful scraping delay
        time.sleep(1)
        
    df = pd.DataFrame(all_quotes)
    df.to_csv('quotes_all_pages.csv', index=False)
    print("Scraping complete! Data successfully saved to 'quotes_all_pages.csv'")

if __name__ == '__main__':
    scrape_quotes()
