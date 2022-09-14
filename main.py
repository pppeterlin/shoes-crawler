##################################################
## Project: {houseoffraser crawler}
## Author: {Chun}
## Version: {220914}
## Status: 
##################################################

import requests
from datetime import datetime
from bs4 import BeautifulSoup
import json, re
import math
#from selenium import webdriver
import pandas as pd


def get_total_num(url):
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
    }
    # url = 'https://www.houseoffraser.co.uk/brand/clarks'
    html = requests.get(url, headers=headers)
    s = BeautifulSoup(html.content)
    n_total = s.find('div', {'id': 'prdlistinformation'}).find('span', {'class': 'totalProducts'}).text
    return(int(n_total))


def gen_api_url(n):
    # https://www.houseoffraser.co.uk/api/productlist/v1/getforcategory?categoryId=HOF_BRACLARKS&page=1&productsPerPage=300
    brand = 'HOF_BRACLARKS'
    page = math.ceil(n/300)
    list_url = []
    prefix = 'https://www.houseoffraser.co.uk/api/productlist/v1/getforcategory?categoryId='+brand
    for i in range(page):
        list_url.append(prefix+'&page='+str(page+1)+'&productsPerPage=300') 

    return(list_url)


def crawl_goods(url):
    # 加入動態ip
    headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
        }
    html = requests.get(url, headers=headers)
    
    return(html)


def get_all_products(html):
    js = json.loads(html.text)
    
    return(js['products'])


def parse_goods(js):
    goods = {
    'productId': None,
    'name': None,
    'price': None,
    'currency': None,
    'on_sale': 0,
    'rate': 0,
    'sizes': None,
    'color': None,
    'url': None
    }
    def parse_price(s):
        currency = s[0]
        price = float(s[1:])
        return({'price': price, 'currency': currency})
    
    def parse_sizes(s):
        sizes = re.findall(r"\((\d+(?:\.\d+)?)\)",s)
        return(sizes)
    
    def parse_url(s):
        prefix = 'https://www.houseoffraser.co.uk'
        return(prefix+s)

    if js:
        goods['productId'] = js['productId']
        goods['name'] = js['name']
        goods['price'] = parse_price(js['price'])['price']
        goods['currency'] = parse_price(js['price'])['currency']
        goods['sizes'] = parse_sizes(js['sizes'])
        goods['color'] = js['colourName']
        goods['colorId'] = js['colourId']
        goods['url'] = parse_url(js['url'])

        if js['discountPercentage']:
            goods['on_sale'] = 1
        
    return(goods)

def get_all_sizes(list_goods):
    l = [s['sizes'] for s in list_goods]
    sizes = set([s for sublist in l for s in sublist])

    return(sizes)



    
if __name__ == '__main__':
    url = 'https://www.houseoffraser.co.uk/api/productlist/v1/getforcategory?categoryId=HOF_BRACLARKS&page=1&productsPerPage=300'
    html = crawl_goods(url)
    products = get_all_products(html)
    list_goods = []
    for p in products:
        list_goods.append(parse_goods(p))

    columns = ['productId', 'gender']
    all_sizes = sorted(list(get_all_sizes(list_goods)))
    columns.extend(all_sizes)
    dt = pd.DataFrame(0, index=range(len(list_goods) ), columns=columns)
    
    for i in range(len(list_goods)):
        s = list_goods[i]
        dt.loc[i, 'productId'] = s['colorId']
        dt.loc[i, s['sizes']] = 1
    