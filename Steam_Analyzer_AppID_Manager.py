import datetime
import pandas as pd

def str2date(string):
    return datetime.datetime.strptime(string, '%Y%m%d')

def date2str(date):
    return datetime.datetime.strftime(date, '%Y%m%d')

def num2days(num):
    return datetime.timedelta(days=num)

class AppIDManager():
    def __init__(self, now_day, duration):
        # set target day
        self.now_day = str2date(now_day)
        # set last target base day
        self.duration = duration
        self.price_file = pd.read_csv('data/applist_for_gameprice.csv')
        self.set_review_files()

    # pre-load the last 30 days review file to speed up computation
    def set_review_files(self):
        self.review_files = []
        for i in range(self.duration):
            days_gap = num2days(self.duration-i)
            date_str = date2str(self.now_day - days_gap)
            review_file = pd.read_csv('data/app_review_result/' + date_str + '.csv')
            self.review_files.append(review_file)
    
    # get last 30 days review by id, return a 30 length array, if data not exist, array will store 0
    def get_reviews(self, id):
        reviews = []
        for i in range(self.duration):
            review_list = self.review_files[i][self.review_files[i]['AppID'] == id].values
            if len(review_list) != 0:
                review = float(self.review_files[i][self.review_files[i]['AppID'] == id]['All Percent'].values[0].strip('%')) / 100
                reviews.append(review)
            else:
                reviews.append(0.0)
        return reviews

    # get last 30 days price by id, return price, if data not exist, will return 0
    def get_price(self, id):
        price_list = self.price_file[self.price_file['AppID'] == id].values
        if len(price_list) != 0:
            price = self.price_file[self.price_file['AppID'] == id]['Price'].values[0]
        else:
            price = 0
        return price

    # get last 30 days people by id, return a 30 length array, if data not exist, array will store 0
    def get_people(self, id):
        people = []
        for i in range(self.duration):
            person_list = self.review_files[i][self.review_files[i]['AppID'] == id].values
            if len(person_list) != 0:
                person = int(self.review_files[i][self.review_files[i]['AppID'] == id]['All People'].values[0].replace(',',''))
                people.append(person)
            else:
                people.append(0)
        return people

    