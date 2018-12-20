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
        self.now_day = str2date(now_day)
        self.duration = duration
        self.price_file = pd.read_csv('data/applist_for_gameprice.csv')
        self.set_review_files()

    def set_review_files(self):
        self.review_files = []
        for i in range(self.duration):
            days_gap = num2days(self.duration-i)
            date_str = date2str(self.now_day - days_gap)
            review_file = pd.read_csv('data/app_review_result/' + date_str + '.csv')
            self.review_files.append(review_file)

    def get_reviews(self, id):
        reviews = []
        for i in range(self.duration):
            review = float(self.review_files[i][self.review_files[i]['AppID'] == id]['All Percent'].values[0].strip('%')) / 100
            reviews.append(review)
        return reviews

    def get_price(self, id):
        price = self.price_file[self.price_file['AppID'] == id]['Price'].values[0]
        return price

    def get_people(self, id):
        people = []
        for i in range(self.duration):
            person = int(self.review_files[i][self.review_files[i]['AppID'] == id]['All People'].values[0].replace(',',''))
            people.append(person)
        return people

    