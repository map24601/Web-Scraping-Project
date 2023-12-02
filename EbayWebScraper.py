import requests
from bs4 import BeautifulSoup
import pandas as pd

searchterm = 'lego rivendell'

def get_data(searchterm):
    searchterm = searchterm.replace(' ', '+')
    url = f'https://www.ebay.com/sch/i.html?_from=R40&_nkw={searchterm}&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1'

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def parse(soup):
    productslist = []
    results = soup.find_all('div', {'class': 's-item__info clearfix'})
    notFound = 0
    for item in results:
        solddate = item.find('div', {'class': 's-item__title--tag'})
        
        if solddate == None: solddate = "No sold date"
        else: solddate = solddate.find('span', {'class':'POSITIVE'}).text[5:]

        bids = item.find('span', {'class': 's-item__bids'})
        if bids == None: bids = "No bids"
        else: bids = bids.text
        product = {
            'title': item.find('div', {'class': 's-item__title'}).text,
            'soldprice': float(item.find('span', {'class': 's-item__price'}).text.replace('$','').replace(',','').strip().split()[0]),
            'solddate': solddate,
            'bids': bids,
            #'link': item.find('a', {'class': 's-item__link'})['href'],
        }
        productslist.append(product)
    print(productslist[0:5])
    return productslist

def output(productslist, searchterm):
    productsdf = pd.DataFrame(productslist)
    productsdf.to_csv(searchterm + ' output.csv', index=False)
    print('Saved to CSV')
    return


soup = get_data(searchterm)
productslist = parse(soup)
parse(soup)
output(productslist, searchterm)
