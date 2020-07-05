import requests
from bs4 import BeautifulSoup
import shopify


# API connection--------------------------------------------------------------------------------------------------
API_VERSION = '2020-7'
SHOP_NAME = 'fost2a'
API_KEY = '5c27637b28787a5217308728c6797a20'
API_PASSWORD = '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'
shop_url = "https://%s:%s@%s.myshopify.com/admin" % (API_KEY, API_PASSWORD, SHOP_NAME)
shopify.ShopifyResource.set_site(shop_url)
shop = shopify.Shop.current()

# scrapping site---------------------------------------------------------------------------------------------------
page = requests.get("https://ar-sa.namshi.com/buy-ella-dotted-sheer-sleeve-top-w757055a.html")
soup = BeautifulSoup(page.content, 'html.parser')
con = soup.find('div', class_='site_width_container')
res = con.findAll('div', class_='content')
for result in res:
    # and dont forget to get the SKU of the product it's important
    # it's a string and you can send it to shopify using
    # product.sku = "<your scrapped sku>"
    # and place it for every variant using
    # variant.sku = "<your scrapped sku>"
    title = result.find('div',class_='product__options').find('h2', class_='product__brandname').text
    des=result.find('div',class_='product__options').find('h1',class_='product__name').text
    print(title,des)
    images =[]
    imageContainer = result.findAll('div',class_='slim-slide zoom')
    for img in imageContainer :
         r=img.find('img')
         rt=r.get('src')
         images.append(rt)
    print(images)
    Scrapsku=result.find('table',class_='product_attributes').text.strip('\t *').splitlines()
    Scrapsku[:] = [item for item in Scrapsku if item != '']
    print(Scrapsku)
    sku=Scrapsku[1]
    print(sku)
    Model_type=Scrapsku[7]
    print(Model_type)
    sizes=result.find('div',class_='size__selector animated').find('ul').text.splitlines()
    sizes[:] = [item for item in sizes if item != '']
    print(sizes)
    pricestandard = str(result.find('p', class_='product__price').find('span').text.strip())
    print(pricestandard)

#add product---------------------------------------------------------------------------------------------------
product = shopify.Product()
product.title = title
product.product_type = Model_type
product.body_html= des
product.sku = sku
variants = []
for size in sizes:
    v = shopify.Variant()
    v.option1 = size
    v.price = pricestandard
    v.sku=sku
    variants.append(v)
product.variants = variants
product.options = [
    {"name": "Size", "values": sizes,"sku":sku}
]
product.images = images
success = product.save()

if product.errors:
    print(product.errors.full_messages())
