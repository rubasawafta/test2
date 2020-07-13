import requests
from bs4 import BeautifulSoup
import shopify
from selenium import webdriver
import re
'''''''''
# Home page API connection-----------------------------------------------------------------------------------------------------
API_VERSION = '2020-7'
SHOP_NAME = 'fost2a'

Urls=[]
shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, API_PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()
page = requests.get("https://il.shein.com/Plus-Size-Dresses-c-1889.html")
soup = BeautifulSoup(page.content, 'html.parser')
con = soup.find('div', class_='j-list-cate-inner')
res = con.findAll('div', class_='c-goodsitem')
c=0
#scraping Home page ---------------------------------------------------------------------------------------------------------------------
for result in res:
   links=result.find('div',class_='c-goodsitem__absolute')
   u=result.find('div',class_='c-goodsitem__ratiowrap')
   url=result.find('a',class_='c-goodsitem__ratioimg')
   href=str (url.get('href'))
   Urls.append(href)
page.close()
'''''
# Product Page API connection ---------------------------------------------------------------------------------------------------
API_VERSION = '2020-7'
SHOP_NAME = 'fost2a'

shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, API_PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()
# scraping Product page --------------------------------------------------------------------------------------------
#for i in Urls:
    #to ='https://il.shein.com'+i
    #print(to)
# page2 = requests.get(to)
browser = webdriver.PhantomJS()
browser.get('https://il.shein.com/Plus-Button-Front-Rolled-Sleeve-Dress-p-1346379-cat-1889.html')
html = browser.page_source
soup2 = BeautifulSoup(html, 'html.parser')
con2 = soup2.find('div', class_='j-goods-detail-v2')
set2 = con2.find('div', class_='goods-detailv2')
contener = set2.find('div', class_='product-intro')
#sku= contener.find('div', class_='product-intro__head-sku').text
title=contener.find('div',class_='product-intro__head-name').text
price=str(contener.find('div',class_='product-intro__head-price').find('span').text)
pricenow =str(re.findall('[0-9]+', price))
size = contener.find('div',class_='product-intro__size-choose').findAll('span',class_='inner')
sizes =[]
for i in size :
  size1 = str(i.text.strip())
  sizes.append(size1)
  sizes1 = [item for item in sizes if item !='']
images = []
image = contener.find('div',class_='swiper-wrapper').findAll('div',class_='swiper-slide')
for i in image :
  r = i.find('img')
  rt = r.get('src')
  images.append({"src":rt})
print(images)

#add product---------------------------------------------------------------------------------------------------
product = shopify.Product()
print('Hiiiii')
product.title = title
#product.product_type = Model_type
#product.body_html= des
product.vendor='fost2a'
#product.sku = sku
variants = []
for size in sizes:
    v = shopify.Variant()
    v.option1 = size.strip()
    v.price =pricenow
    #v.sku=sku
    variants.append(v)
product.variants = variants
product.options = [
    {"name": "Size", "values": sizes1}
]
product.images = images
success = product.save()

if product.errors:
    print(product.errors.full_messages())



