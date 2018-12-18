import requests
from bs4 import BeautifulSoup
import re
import csv
import time

filename = 'applist_for_review_20181031'
result_filename = 'applist_for_gametype'

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

def get_types(html):
    types = []
    game_areas = html.find_all('div', {'class': 'details_block'})
    links = game_areas[0].find_all('a')
    for link in links:
        if match_string('/genre/', link['href']) != '':
            types.append(link.text)
        else:
            break
    return types

with open(filename + '.csv', newline='') as csv_file:
    the_reader = csv.reader(csv_file)
    with open(result_filename + '.csv', 'w') as csv_result:
        the_writer = csv.writer(csv_result)
        
        cc = 0
        for row in the_reader:
            appid = row[0]
            name = row[1]

            if cc == 70000:
                break

            try:     
                html = get_html('https://store.steampowered.com/app/' + appid)
                # html = get_html('https://store.steampowered.com/app/524220')
                title = get_title(html)
                if title[len(title)-8:len(title)] == "on Steam":
                    types = get_types(html)
                    the_writer.writerow([appid] + types)
                    print(cc, appid, name, types)
                else:
                    print(cc, "+++++", title, "-----", name, "=====", appid)
            except:
                print(cc,"not exist", appid, ":", name)
            time.sleep(0.01)
            cc +=1
            #break