import datetime

class AppIDManager():
    def __init__(self, now_day, duration):
        self.one_day = datetime.timedelta(days=1)
        self.now_day = self.str2date(now_day)
        self.duration = duration

    def get_review(self, id):
        pass

    def get_price(self, id):
        pass

    def get_people(self, id):
        pass

    def str2date(self, string):
        return datetime.datetime.strptime(string, '%Y%m%d')

    def date2str(self, date):
        return datetime.datetime.strftime(date, '%Y%m%d')