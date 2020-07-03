import requests
from bs4 import BeautifulSoup
import  os
import shopify
import re

# API connection

API_VERSION = '2020-7'
SHOP_NAME= 'fost2a'
shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()



# scrapping site
page = requests.get("https://www.nastygal.com/tie-romance-with-me-puff-sleeve-culotte-jumpsuit/AGG47758-2.html?color=165")
soup = BeautifulSoup(page.content, 'html.parser')
con = soup.find('div', class_='pdp-main')
res = con.findAll('div', class_='pdp-main-inner')
for result in res:
       title = result.find('h1', class_='product-name').text.strip()
       pricestandard = result.find('span', class_='price-standard').text.strip()
       img = result.find('div', class_='product-col-1 product-image-container')
       pricesales = result.find('span', class_='price-sales').text.strip()
       size = result.find('div' ,class_='attribute size-attribute').find('ul',class_='swatches size clearfix').text
     #  print (title,pricestandard, pricesales,size)

product= shopify.Product()
{
  "product": {
    "title": title,
    "body_html": "<strong>Good snowboard!</strong>",
    "vendor": "fost2a",
    "product_type": "Snowboard",
    "variants": [
      {
        "option1": "Blue",
        "option2": "155"
      },
      {
        "option1": "Black",
        "option2": "159"
      }
    ],
    "options": [
      {
        "name": "Color",
        "values": [
          "Blue",
          "Black"
        ]
      },
      {
        "name": "Size",
        "values": [
          "155",
          "159"
        ]
      }
    ]
  }
}

success = product.save()




