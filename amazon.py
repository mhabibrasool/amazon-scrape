# Data scraping effort from amazon.py

import requests
from bs4 import BeautifulSoup as bs4

from urllib.parse import urlencode

from pprint import pprint

url = 'https://www.amazon.com/s?k=aerospace+engineering'

api_key = 'YOUR_API_KEY'

payload = {
    'api_key' : api_key,
    'url' : url
}

response = requests.get('https://api.scraperapi.com/', params=payload)

soup = bs4(response.content, 'html.parser')


### Ask soup for link for all products in first page. ###
links = soup.findAll('a', {'class': 'a-link-normal'})

### Ask soup for link for next page ( for this case it is second page)
second_page = soup.find('a', {'class': 's-pagination-item'}).get('href')

### Ask soup for link for all pages in amazon.
#  all_pages = soup.findAll('a', {'class': 's-pagination-item'})

### Ask soup for title of the products
product_title = soup.find_all('div', {'class': 's-result-item'})


for product in product_title:
    try:
        
        title = product.find('span', {'class': 'a-color-base'}).text
        star = product.find('span', {'class': 'a-icon-alt'}).text
        num_of_reviews = product.find('span', {'class': 'a-size-base s-underline-text'}).text
        mode = product.find('div', {'class': 'a-row a-size-base a-color-base'}).find('a').text
        price = product.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text
        if len(title.split()) > 3 and '$' not in mode:
            print(title, star, num_of_reviews, mode, price)
        elif len(title.split()) > 3:
            print(title, star, num_of_reviews, price)
        else:
            pass
    except:
        pass