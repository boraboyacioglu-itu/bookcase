# Author: Bora Boyacıoğlu (github.com/boraboyacioglu-itu)

import re
import requests
from bs4 import BeautifulSoup

# The mapping of digit words to their integer values.
DIGIT_MAPPING = {
    'One'  : 1,
    'Two'  : 2,
    'Three': 3,
    'Four' : 4,
    'Five' : 5,
}

def get_soup(url: str) -> BeautifulSoup:
    """ Get the HTML content of a webpage. """
    response = requests.get(url)
    
    # Raise an exception for bad status codes.
    response.raise_for_status()
    
    return BeautifulSoup(response.text, 'html.parser')

def parse(url: str) -> dict[str, str | int | float]:
    """ Parse the book page. """
    
    soup: BeautifulSoup = get_soup(url)
    
    results: dict[str, str | int | float] = {
        'title' : '' ,
        'price' : 0.0,
        'stock' : 0  ,
        'desc'  : '' ,
        'rating': 0  ,
    }
    
    """
    Extract the title.
    """
    title = soup.find('h1')
    if title:
        results['title'] = title.text.strip()
    
    """
    Extract the price.
    """
    price = soup.find('p', class_='price_color')
    if price:
        # Remove the currency symbol.
        results['price'] = float(re.sub(r'[^\d.]', '', price.text))
    
    """
    Extract the stock info.
    """
    stock = soup.find('p', class_='instock availability')
    stock_chck = soup.find('i', class_='icon-ok')
    if stock and stock_chck:
        # Extract the stock count from the format:
        # "In stock (XX available)"
        results['stock'] = int(re.sub(r'[^\d]', '', stock.text))

    """
    Extract the description.
    """
    # The description is not directly labeled,
    # instead, it comes right after the div with the id "product_description".
    desc_h = soup.find('div', id='product_description')
    if desc_h:
        desc = desc_h.find_next_sibling('p')
        if desc:
            results['desc'] = desc.text.strip()
            
    """
    Extract the rating.
    """
    rating = soup.find('p', class_='star-rating')
    if rating:
        # The rating element has another class,
        # which is the rating value in words.
        rating_class = rating.get('class', [])[1]  # type: ignore
        if rating_class in DIGIT_MAPPING:
            results['rating'] = DIGIT_MAPPING[rating_class]
    
    return results