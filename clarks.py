##################################################
## Project: {houseoffraser crawler}
## Author: {Chun}
## Version: {220913}
## Status: 
##################################################

from email import header
import os, platform
import requests
from datetime import datetime
from bs4 import BeautifulSoup
#from selenium import webdriver
import time, re


# Clarks
def next_page():
    #use dppp=300
    return(html)

def crawl_page(url):
    headers={"User-Agent": "Mozilla/5.0 (X11; CrOS x86_64 12871.102.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.141 Safari/537.36"}
    html = requests.get(url, headers=headers)   
    return(html)

def parse_page(html):
    soup = BeautifulSoup(html.content)
    s = soup.find('div', {'id': 'productlistcontainer'})
    s = s.findAll('li')

    goods_list = []
    if len(s):
        for i in s:
            goods_list.append(crawl_goods(i))
    
    return(goods_list)


def crawl_goods(li):
    goods = {
        'name': None,
        'brand': None,
        'productID': None,
        'link': None,
    }
    if li:
        atr = li.attrs
        goods['name'] = atr['li-name']
        goods['brand'] = atr['li-brand']
        goods['productID'] = atr['li-productid']
        goods['link'] = atr['li-url']
    
    return goods


def parse_goods(goods_url):
    goods = {
        'productID': None,
        'price': None,
        'on_sale': 0,
        'rate': 0,
        'size': None,
        'color': None
    }

    def parse_id(soup):
        t = soup.find('p', {'id': 'lblProductCode'}).text
        t = t.split(': ')[1].split('\r')[0]
        return(t)

    def parse_rate(soup):




if __name__ == '__main__':


url = "https://www.houseoffraser.co.uk/brand/clarks#dcp=1&dppp=300&OrderBy=rank"
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
            "Cookie": 'X-Origin-Cookie=1; segment_anonymous_id=a945c6a7-a706-495b-acb4-ad0925ffcd37; RT="z=1&dm=houseoffraser.co.uk&si=bb360d18-1dfa-4d51-9b0d-7c806cb185c3&ss=l8056hjj&sl=0&tt=0&bcn=%2F%2F684d0d45.akstat.io%2F&ld=4j2gc&ul=lyl&hd=mey"; _abck=AB054D5DBCFE83F69216EFF5909D51BD~0~YAAQtMdCy9w+CjaDAQAAsvS4Nggw1OMxAehZEMPGKyFyb7SomJ4cxHcACv0bT0/3MK7p4U8/tfLSKPjneqYjNIfmgfzOEd0kH9eFUV2kEKj9cRuk8YAfTKOdw02nm6XNOWSvdhL9jWgFlwQM69cHi3gAMlYyq4yp1zDgVdokE816XuHkNMW7VUFVCT5qfkOXbiEi0E5PqKUswLnIeoo70H9rVHNdJHq8Sp7c1fxoSP5X2dIKZ822XoSdiYw9/yE7ztWbkow9PMByXXdmb/D5atpa0ITo5qSsFjAirR9hOEZr/niRclqPA5cIpnqeZDbegVt/cG11jwQzGsRE8tzVAO64A2JVSTdaobzkDNT3okd5c5Lc2DDR/793nSOv6McvZaJeTQ==~-1~-1~-1; bm_sv=BD44E8D492FA27EE8CCCD65F5321332F~YAAQtMdCy90+CjaDAQAAsvS4NhEUG3l8pXebSJ5rCjXIwygJL7qq/7QlrX1yTYbcEhvRvCWNTzZVTXNsU/GMYQecQjgyTsnn6q/RXwgT60v7PZqoPNUYj/rcFKm6v6+UjS3zLX1VBkFJAC/u7QJht31jZYimVBiMSS+NX8v83/8AewaZ0PTQsSrN70C5GIXhDpDNDu4R+CcTgXLj7e94fG67qncK6lUL8B2WKOwa+IonHccQegkd+OwjfM23fVufjmIjB4TfqqUo~1; dtPC=2$470409174_779h-vCLQVURHVNVICMANQKTTQMMUHPSHSMKUK-0e0; TS01a19d95=01e4dc9a76342c989025c1fc044e17c016243094e928d4fb3ec3b28a8ca476d7cb87b87ef093334649cff8f017ffce8acaf929a562cd3625b2a07b39c653421a67e723f5bd2e69bb3a0184187a4c83f5fe23366204f95f45e80e907cc0bcc7ead1524de0a5a3152fa90258c30ea26d599b40088701988b1e53a66143e3e855909810ccaf2649adcdeace34c8cf3820c745953a5ebad0fc1a8bd2095c5f30f3c5d208e832e2; _dyid_server=1702361532687456769; dtCookie=v_4_srv_2_sn_58A0EM3BEHS1B5MT40PGA2ULQ5T0Q1KT_app-3Af0ca7b91118eaa5d_1_ol_0_perc_100000_mul_1_rcs-3Acss_0; dtSa=-; rxvt=1663072233695|1663067835637; QuantumMetricSessionID=0d4d37a675109664e63c7e49a68b0998; _ga_QMPM2M8PCP=GS1.1.1663068829.5.1.1663070426.0.0.0; rxVisitor=1663048193535DH3UEM452APB0BOGDTLOOKHL4K8QLHKG; QuantumMetricUserID=faee1de5173ec4a35141d4a4c84d348b; _clsk=mnsx7s|1663070411024|7|1|j.clarity.ms/collect; _pin_unauth=dWlkPU1UVTRNV0poTXpJdFpqQmxOeTAwT0RjNExUZ3hNMkl0WmpJNU4yUTNOemcwT1dVdw; _fbp=fb.2.1663048193737.690851555; ajs_anonymous_id=a945c6a7-a706-495b-acb4-ad0925ffcd37; scarab.profile=%2211948203-1286479%7C1663070410%7C11948105-1286477%7C1663069733%7C02358903-1372168%7C1663068830%7C23332803-1334608%7C1663061388%7C02140606-1377513%7C1663054854%7C11674105-1334263%7C1663054174%7C23938906-1334299%7C1663053962%7C23938903-1334299%7C1663053443%7C11804303-1334277%7C1663048358%22; scarab.visitor=%224B170F4949B6B2AA%22; _cq_duid=1.1663048191.GypfqpmgZeoc4Czc; _cq_suid=1.1663048191.bCoaox8C5V2CK9J9; _dy_c_exps=; _dy_df_geo=Taiwan..Taipei%20City; _dy_geo=TW.AS.TW_TPE.TW_TPE_Taipei%20City; _dy_soct=1033308.1066950.1663068829.i9awp8mokjg95gc21dlocw681tmu7vdd*1020021.1035684.1663070409*1105303.1314879.1663070409*1055929.1140410.1663070409*1077944.1231916.1663070409; _dy_toffset=0; _dycnst=dg; _dycst=dk.m.s.ws.; _dyid=1702361532687456769; _ga=GA1.3.527195457.1663048191; _gid=GA1.3.1443313740.1663048193; _uetsid=45d7aa00332811eda333e9c0c52699a0; _uetvid=45d7d470332811edbdc3117d83fa1f0e; dtLatC=114; _dy_c_att_exps=; _dy_csc_ses=i9awp8mokjg95gc21dlocw681tmu7vdd; _dyjsession=i9awp8mokjg95gc21dlocw681tmu7vdd; OptanonConsent=isGpcEnabled=0&datestamp=Tue+Sep+13+2022+20%3A00%3A08+GMT%2B0800+(%E5%8F%B0%E5%8C%97%E6%A8%99%E6%BA%96%E6%99%82%E9%96%93)&version=202208.1.0&isIABGlobal=false&hosts=&consentId=b0a0b6a0-05e5-49e4-af9e-04c60de3c4a5&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=TW%3BTAO&AwaitingReconsent=false; selectedLevel2MenuTabId=0; BVBRANDSID=b60d19ad-5c42-47a6-a2a1-da18bc34a5aa; ak_bmsc=E00AE225B40CABCB34C1481D35842DF6~000000000000000000000000000000~YAAQTV9Ky0D0DwCDAQAANHegNhHLBbinft5LQaXaHlNn8UUpmnQaLNFfvUGHER/slCCiq/X03IFScSGOINMSs9v3tdtrLyeP3JhU2p9fUUC2nTpHuICLomoBCQxE4i9dcEP/8jeQLHNrFIoHh3eOe0+lMTnZNv5k5D04G97oKpt/xAGElaLqcSbBCZi4TY0ES+KZsnCNaOJeiyd/4xHNmdHXyN13dGw476N4SfZB2SXt+EV6iOPbPeU8vho5cIa7P7ag2reWarurbJjBikPK+wUMqlwhyIwGQmPCDecB7yAz85GcsKFKBfXvjZ/RL46Zs4DtWyRFuYXlQpuCktOMDYSMFqAzo/E3sNIayQmZNKRPiB+CztwodzT1oyYjZyEJ5nTUlp40fuz/b6UPwBXCO4LpZzKVAi/WmhbL3+4WWwZUT1Jg26p1Nk/FoGbZdzRclKT3AXcnHzvlgyIEYfj7tD1s/Sz7wz0UOsoGO8NgFbtvDrIUMS/ay84mfAbGs7FM4MS33B1Xg/SWd8DjKyrwyI0q3hVFUMkQblcEuG8z; dy_fs_page=www.houseoffraser.co.uk%2Fbrand%2Fclarks%2Fclarks-grip-trade-ch00-023589; segment_anonymous_id=35d7367e-beeb-4d2a-8242-6da0bb222367; _gcl_au=1.1.269155970.1663062315; bm_sz=EBCCE7F49FA7312E87F67C6554A1E308~YAAQTV9KyynoDwCDAQAAgaItNhGM8MkhnGHBnEGV0C2dkO5IoD2xh+yzRdk6EkHaPHwPbu4l2B4BRvecE3D7bXNc++Z/lg/vttUC7IDmCG2FiH1KsYmZuJk+6QX7UaFavrwFRGAhmnwbT+vsYPmNbkr8Qa0lzKOpcqOnTgNmAJy0p/VIn9hr2yYq7mxumQmMAlKHIPa1gz01Qk9FybrqC44xr6ysH8HD18u/u5YcKJURyl6NqWADsMEUB1SPJOEjYAExb05Vvs8DZHttvXyAfSVUTpKIpUDve5WCPP3SNBq4oc5mNCh+sU9C6UB1UQshmY8Te0kOmTlfhizQKOmApnkFigY=~3487540~4601157; _clck=1ygoyu9|1|f4u|0; BVImplmain_site=13808; _dyfs=1663049640605; ChosenSite=www.houseoffraser.co.uk; CountryRedirectCheckIsDone=true; OptanonAlertBoxClosed=2022-09-13T05:49:53.273Z; BVBRANDID=95985bba-9d1f-4ade-96bd-42725168eb77; _ALGOLIA=anonymous-5d5e56e6-9f21-491a-b79a-5ed18e1fbdaa; TS0190aaa8=01e4dc9a76d1f8771e02fd38f3179e47766ea1fa05a36f1d84c7957b4e397eca2d907a6ac7c04b1d37f6187222dd44272345f75263dece9455d07b36cb71859afb6a5f60c6; T_ch_50=AL; HouseOfFraser_AuthenticationCookie=184f3955-4e2a-47ed-9aee-8494cf6b7b40; X-SD-URep=0bd589c9-ca49-4977-8442-2ce68b33faad'
        }
html = requests.get(url, headers=headers)    
# html = requests.post(url, headers=headers)    
with open("response.txt", "w") as f:
    f.write(html.text)

soup = BeautifulSoup(html.content)

s1 = soup.find('div', {'id': 'productlistcontainer'})
l = s1.findAll('li')
    print(i.text)



url = "https://www.houseoffraser.co.uk/brand/clarks#dcp=1&dppp=300&OrderBy=rank"
html = crawl_page(url)
results = parse_page(html)

prefix = 'https://www.houseoffraser.co.uk'
url = prefix+results[0]['link']
html = requests.get(url, headers=headers)
with open("response.txt", "w") as f:
    f.write(html.text)

soup = BeautifulSoup(html.content)
soup.find('p', {'id': 'lblProductCode'}).text
soup.find('div', {'id': 'divColourImages'})


s = requests.Session()
url = "https://www.houseoffraser.co.uk/brand/clarks#dcp=1&dppp=36&OrderBy=rank"
headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
        }
s.get(url, headers=headers)

url = 'https://www.houseoffraser.co.uk/api/productlist/v1/getforcategory?categoryId=HOF_BRACLARKS&page=1&productsPerPage=300&sortOption=rank&selectedFilters=&isSearch=false&searchText=&columns=4&mobileColumns=2&clearFilters=false&pathName=%2Fbrand%2Fclarks&searchTermCategory=&selectedCurrency=GBP&portalSiteId=318&searchCategory='

payload = { "productsPerPage": "300",
        }
# categoryId: HOF_BRACLARKS
# page: 1
# productsPerPage: 300
# sortOption: rank
# selectedFilters
# isSearch: false
# searchText
# columns: 4
# mobileColumns: 2
# clearFilters: false
# pathName: /brand/clarks
# searchTermCategory
# selectedCurrency: GBP
# portalSiteId: 318
# searchCategory
html = s.post(url, headers=headers, data=payload)

html = requests.get(url, headers=headers)
with open("api_response.txt", "w") as f:
    f.write(html.text)

import json
js = json.loads(html.text)


url_adidas = 'https://www.houseoffraser.co.uk/api/productlist/v1/getforcategory?categoryId=HOF_TMBADIDAS&page=1&productsPerPage=300&sortOption=rank&selectedFilters=&isSearch=false&searchText=&columns=4&mobileColumns=2&clearFilters=false&pathName=%2Fmen%2Fadidas&searchTermCategory=&selectedCurrency=GBP&portalSiteId=318&searchCategory='
https://www.houseoffraser.co.uk/api/productlist/v1/getforcategory?categoryId=HOF_TMBADIDAS&page=2&productsPerPage=300&sortOption=rank&selectedFilters=&isSearch=false&searchText=&columns=4&mobileColumns=2&clearFilters=false&pathName=%2Fmen%2Fadidas&searchTermCategory=&selectedCurrency=GBP&portalSiteId=318&searchCategory=

for i in range(1, 5):
    print(js['products'][i]['name'])