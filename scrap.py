import requests
from bs4 import BeautifulSoup
import  os
import shopify
import re

# API connection

SHOP_NAME= 'fost2a'
shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()

# connection test
product = shopify.Product.find(5275133477027)
print(bool(shopify.Product.find(5275133477027)))
product.price = 15 ;


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




# Create a new product
new_product= shopify.Product()
new_product.title =title
new_product.size=size
new_product.vendor = "fost2a"
success = new_product.save()




