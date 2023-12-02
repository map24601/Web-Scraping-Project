import csv

from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

def check_price():
    URL = 'https://www.amazon.com/JBL-Tune-510BT-Ear-Headphones/dp/B08WM3LMJF/?_encoding=UTF8&pd_rd_w=mcYz7&content-id=amzn1.sym.8c43194a-ac6b-471a-b5f2-8e9d449246f2&pf_rd_p=8c43194a-ac6b-471a-b5f2-8e9d449246f2&pf_rd_r=AFTSMZ4AZZHNDS643FP1&pd_rd_wg=I03ub&pd_rd_r=5eb0f30d-0873-43f4-b2a3-ae8d0714bdb8&ref_=pd_gw_dealz_sv&th=1'

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

    page = requests.get(URL, headers=headers)

    soup1 = BeautifulSoup(page.content, "html.parser")

    soup2 = BeautifulSoup(soup1.prettify(), 'html.parser')

    title = soup2.find(id='productTitle').get_text()
    title=title.strip()
    priceHolder = soup2.find(id='tp-tool-tip-subtotal-price-value').get_text()
    price = priceHolder.split()[0][1:]
    
    #import datetime
    today = datetime.date.today()

    #import csv

    header=['Title', 'Price', 'Date']
    data=[title, price, today]

    with open('AmazonWebScraperDataset.csv', 'a', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)

