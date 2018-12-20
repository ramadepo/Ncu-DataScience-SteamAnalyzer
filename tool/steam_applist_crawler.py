import requests
import json
import csv

filename = "applist_20181219"

def get_api_response(web_url):
    reponse = requests.get(web_url)
    return reponse

with open( filename + '.json', 'w') as json_file:
    app_list = get_api_response("https://api.steampowered.com/ISteamApps/GetAppList/v2/")
    json_file.write(app_list.text)


with open(filename + '.csv', 'w') as csv_file:
    the_writer = csv.writer(csv_file)
    
    with open(filename + '.json', 'r') as json_file:
        app_list = json.load(json_file)
        app_count = 0
        for app in app_list['applist']['apps']:
            the_writer.writerow([app["appid"], app["name"]])
            app_count += 1
        print(app_count)