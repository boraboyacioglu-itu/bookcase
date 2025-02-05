# Author: Bora Boyacıoğlu (github.com/boraboyacioglu-itu)

# import AnsiLib as al  # My own library for coloured text.
import json
import time  # For sleeping between requests.

import requests
from urllib.parse import urljoin

from utils import parser

def scrape(base_url: str) -> list[dict[str, str | int | float]]:
    """
    Scrape the books from the given URL.
    
    Args:
        base_url (str): The base URL to scrape.
        
    Returns:
        list[dict[str, str | int | float]]: A list of dictionaries containing the scraped data.
    """
    
    books: list[dict[str, str | int | float]] = []
    
    # Scrape the first page.
    url: str = base_url
    page_id: int = 0
    while url:
        soup = parser.get_soup(url)
        
        # Get all the books.
        articles = soup.find_all('article', class_='product_pod')
        for i, article in enumerate(articles):
            print(f"\rPage: {page_id + 1}, Book: {i + 1}/{len(articles)}", end=' ' * 5)

            # The link to the page of the book.
            rel_link: str = article.find('h3').find('a').get('href')  # type: ignore
            
            # Build the absolute URL.
            book_url = urljoin(url, rel_link)
    
            try:
                # Parse the book page.
                book = parser.parse(book_url)
                if book:
                    books.append(book)
            except requests.exceptions.HTTPError:
                print(f"Failed to scrape: {book_url}")
                
            # Sleep to avoid getting banned.
            # time.sleep(0.1)

        # Get the next page.
        next_page = soup.find('li', class_='next')
        if next_page:
            next_link: str = str(next_page.find('a').get('href'))  # type: ignore
            url = urljoin(url, next_link)
            page_id += 1
        else:
            url = ''

    print()
    return books

def main():
    base_url = 'http://books.toscrape.com/'
    
    # Scrape the books.
    books = scrape(base_url)
    
    # Save the data to a JSON file.
    with open('books.json', 'w', encoding='utf-8') as f:
        json.dump(books, f, indent=4)

if __name__ == '__main__':
    main()