import requests
from bs4 import BeautifulSoup
import re
import csv
import time

filename = 'applist_for_gametype'
with open(filename + '.csv', newline='') as csv_file:
    the_reader = csv.reader(csv_file)
    typelist = []

    for row in the_reader:
        for the_type in row[1:]:
            if the_type not in typelist:
                typelist.append(the_type)
with open('typelist.csv', 'w') as csv_file:
    the_writer = csv.writer(csv_file)
    for i in typelist:
        the_writer.writerow([i])
print(len(typelist), typelist)