# -*- This Program is written with an effort to scrape product data from 
#      amazon.com (amazon) by a given word.  

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


def request_function(url):
      response = requests.get(url)
      html = bs4(response.content, 'html.parser')
      return html

class Scraper:
            
      def parse(html_doc):
            """ Ask the required product data from page ::
            #   title of product, star given that product
            #   total number of reviews and price of that product.
      
            """ 
            ###  Ask the required product data from page ::
            #   title of product, star given that product
            #   total number of reviews and price of that product.

            # Launch an empty list
            product_listing = []
            # Get all products in this page
            product_listings = html_doc.findAll('div', {'class': 's-result-item'})
            for listing in product_listings:
                  try:
                        title = listing.find('span', {'class': 'a-color-base'}).text
                        star = listing.find('span', {'class': 'a-icon-alt'}).text
                        num_of_reviews = listing.find('span', {'class': 'a-size-base s-underline-text'}).text
                        mode = listing.find('div', {'class': 'a-row a-size-base a-color-base'}).find('a').text
                        price = listing.find('span', {'class': 'a-price'}).find('span', {'class': 'a-offscreen'}).text
                        url = 'https://amazon.com' + listing.find('div', {'class': 'a-section a-spacing-none a-spacing-top-small s-title-instructions-style'}).find('a').get('href')
                        product_data = {
                              'title' : title, 
                              'star' : star,
                              'Number of Reviews' : num_of_reviews,
                              'mode' : mode,
                              'price' : price,
                              'URL' : url
                        }
                        product_listing.append(product_data)
                        print(title, star, mode, price, url)
                  except:
                        pass
                  #if len(title.split()) > 3 and '$' not in mode:
            return len(product_listing)
                        
      def main():
            response = requests.get('https://api.scraperapi.com/', params=payload)
            soup  = bs4(response.content, 'html.parser')
            result = self.parse(soup)
            print(result)




      if __name__ == '__main__':
            main()