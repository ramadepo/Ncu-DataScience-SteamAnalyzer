import requests
from bs4 import BeautifulSoup
import re
import csv
import time

filename = "applist_for_review_20181031"
result_filename = 'applist_for_review_20181218'

def match_string(pattern, string):
    return re.search(pattern, string).group(0)

def get_html(web_url):
    response = requests.get(web_url)
    html = BeautifulSoup(response.text, 'html.parser')
    return html

def get_review(html):
    review = {}
    
    summary_col = html.find_all('div', {'class': 'summary column'})
    kind = 'no review'
    evaluation = []
    people = []
    percent = []
    result = []
    for result_set in summary_col:
        # need more review
        tmp = result_set.find('span', {'class': 'game_review_summary not_enough_reviews'})
        if tmp != None:
            kind = 'need more'
            people.append(match_string('[0-9,]+', str(tmp.text)))
            percent.append('None')
            evaluation.append('None')
            result.append(tmp)
            break
        # have positive review
        tmp = result_set.find('span', {'class': 'game_review_summary positive'})
        if tmp != None:
            kind = 'positive'
            responsive = result_set.find('span', {'class': 'responsive_hidden'}).text
            people.append(match_string('[0-9,]+', str(responsive)))
            nonresponsive = result_set.find('span', {'class': 'nonresponsive_hidden responsive_reviewdesc'}).text
            percent.append(match_string('[0-9]+%', str(nonresponsive)))
            evaluation.append(tmp.text)
            result.append(tmp)
        # have negitive review
        tmp = result_set.find('span', {'class': 'game_review_summary '})
        if tmp != None:
            kind = 'negitive'
            responsive = result_set.find('span', {'class': 'responsive_hidden'}).text
            people.append(match_string('[0-9,]+', str(responsive)))
            nonresponsive = result_set.find('span', {'class': 'nonresponsive_hidden responsive_reviewdesc'}).text
            percent.append(match_string('[0-9]+%', str(nonresponsive)))
            evaluation.append(tmp.text)
            result.append(tmp)
        # have mixed review
        tmp = result_set.find('span', {'class': 'game_review_summary mixed'})
        if tmp != None:
            kind = 'mixed'
            responsive = result_set.find('span', {'class': 'responsive_hidden'}).text
            people.append(match_string('[0-9,]+', str(responsive)))
            nonresponsive = result_set.find('span', {'class': 'nonresponsive_hidden responsive_reviewdesc'}).text
            percent.append(match_string('[0-9]+%', str(nonresponsive)))
            evaluation.append(tmp.text)
            result.append(tmp)

    if kind == 'no review':
        review['All Review'] = 'None'
        review['All Percent'] = 'None'
        review['All People'] = 'None'
    else:
        length = len(result)
        review['All Review'] = evaluation[length-1]
        review['All Percent'] = percent[length-1]
        review['All People'] = people[length-1]
    
    return review

def get_title(html):
    return str(html.find('title').text)

with open(filename + '.csv', newline='') as csv_file:
    the_reader = csv.reader(csv_file)
    with open(result_filename + '_result.csv', 'w') as csv_result:
        the_writer = csv.writer(csv_result)
        the_writer.writerow(["AppID", "App Name", "All Review", "All Percent", "All People"])
        
        cc = 0
        for row in the_reader:
            appid = row[0]
            name = row[1]

            if cc == 70000:
                break

            try:     
                html = get_html('https://store.steampowered.com/app/' + appid)
                title = get_title(html)
                if title[len(title)-8:len(title)] == "on Steam":
                    review = get_review(html)
                    the_writer.writerow([appid, name, review['All Review'], review['All Percent'], review['All People']])
                    print(cc, appid, name, review['All Review'], review['All Percent'], review['All People'])
                else:
                    print(cc, "+++++", title, "-----", name, "=====", appid)
            except:
                print(cc,"not exist", appid, ":", name)
            time.sleep(0.01)
            cc +=1