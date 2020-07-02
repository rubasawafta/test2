import requests
from bs4 import BeautifulSoup
import shopify


page = requests.get("https://www.nastygal.com/womens/dresses?cat=dresses")
soup = BeautifulSoup(page.content, 'html.parser')
con = soup.find('ul', class_='search-result-items')
res = con.findAll('li', class_='grid-tile')

for result in res:
      # imag = result.find('div' ,class_='product-image load-bg').text.strip()
       title =  result.find('div', class_='product-tile-name').text.strip()
       pric =result.find('span' ,class_='product-standard-price').text.strip()
       salePrice =result.find('span',class_='product-sales-price' ).text.strip()
       print(title,pric,salePrice)
shop_url = "https://%s:%s@fost2a.myshopify.com/admin/api/%s" % (API_KEY, PASSWORD, API_VERSION)
print(shop_url)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()
