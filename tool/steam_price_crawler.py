import requests
from bs4 import BeautifulSoup
import re
import csv
import time

filename = 'applist_for_review_20181031'
result_filename = 'applist_for_gameprice'

def get_html(web_url):
    response = requests.get(web_url)
    html = BeautifulSoup(response.text, 'html.parser')
    return html

def get_title(html):
    return str(html.find('title').text)

def match_string(pattern, string):
    s = re.search(pattern, string)
    if s == None:
        return ''
    return s.group(0)

def get_price(html):
    price = '0'
    the_price = ''
    game_area_purchase = html.find_all('div', {'id': 'game_area_purchase'})
    price_areas = game_area_purchase[0].find_all('div', {'class': 'game_purchase_price price'})
    if len(price_areas) != 0:
        the_price =  match_string('[0-9,]+', price_areas[0].text)

    if the_price != '':
        price = the_price.replace(',', '')
    else:
        # maybe it's on discount, still crawl the origin price
        price_areas = html.find_all('div', {'class': 'discount_original_price'})
        if len(price_areas) != 0:
            the_price =  match_string('[0-9,]+', price_areas[0].text)
            if the_price != '':
                price = the_price.replace(',', '')
    return price

with open(filename + '.csv', newline='') as csv_file:
    the_reader = csv.reader(csv_file)
    with open(result_filename + '.csv', 'w') as csv_result:
        the_writer = csv.writer(csv_result)
        the_writer.writerow(['AppID', 'Price'])
        cc = 0
        for row in the_reader:
            appid = row[0]
            name = row[1]

            if cc == 70000:
                break

            try:     
                html = get_html('https://store.steampowered.com/app/' + appid)
                #html = get_html('https://store.steampowered.com/app/602520')
                title = get_title(html)
                if title[len(title)-8:len(title)] == "on Steam":
                    price = get_price(html)
                    the_writer.writerow([appid, price])
                    print(cc, appid, name, price)
                else:
                    print(cc, "+++++", title, "-----", name, "=====", appid)
            except Exception as e:
                #print(e)
                print(cc,"not exist", appid, ":", name)
            time.sleep(0.01)
            cc +=1
            #break