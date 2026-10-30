# Web Scraping Quotes Project

A beautiful, clean, and robust Python web scraper built with **BeautifulSoup** and **Requests** to extract quotes, authors, and associated tags across multiple pages from [Quotes to Scrape](https://quotes.toscrape.com/).

## 📋 Project Features
- **Multi-page Traversal**: Automatically paginates through all 10 pages of the target website.
- **Polite Crawling**: Incorporates rate limiting (`time.sleep`) to prevent server overload.
- **Error Handling**: Implements request timeouts and status code validation.
- **Data Export**: Cleans, parses, and saves the extracted tabular data directly to a clean CSV format using `pandas`.

## 🛠️ Tech Stack
- **Python 3.x**
- **Requests**: For making efficient HTTP requests.
- **BeautifulSoup4**: For parsing the HTML content.
- **Pandas**: For structured data extraction and CSV serialization.

## 🚀 Getting Started

### Prerequisites
Make sure you have Python installed, then install the required dependencies:
```bash
pip install requests beautifulsoup4 pandas
```

### Running the Scraper
Execute the main Python script to run the multi-page crawler:
```bash
python scraper.py
```

### Output Dataset Schema
The extracted data is saved to `quotes_all_pages.csv` containing the following attributes:

| Column | Description |
| :--- | :--- |
| **Page** | The source page number where the quote was scraped (1 - 10) |
| **Quote** | The text content of the quote |
| **Author** | Name of the author who said it |
| **Tags** | Comma-separated topics/tags relevant to the quote |

## 📄 License
This project is licensed under the MIT License - feel free to use it as a learning reference!
