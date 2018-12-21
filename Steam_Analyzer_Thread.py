from PyQt5.QtCore import QThread,pyqtSignal
import time

class PlotThread(QThread):
    def __init__(self, plot_manager, tags):
        QThread.__init__(self)
        self.plot_manager = plot_manager
        self.tags = tags
        self.active = True
        
    # self.active imply the thread is alive or not
    def run(self):
        while self.active:
            if self.plot_manager.changed:
                self.plot_manager.plot(self.tags)
            time.sleep(0.0000000000000000000000000000000000000000000001)

    def stop(self):
        self.active = False
        self.wait()

class PredictThread(QThread):
    done = pyqtSignal()
    def __init__(self, plot_manager, appid_manager, apps, duration):
        QThread.__init__(self)
        self.plot_manager = plot_manager
        self.appid_manager = appid_manager
        self.apps = apps
        self.duration = duration

    def run(self):
        total_people = [0] * self.duration
        total_price = [0.0] * self.duration

        # calculate total number of people
        for appid in self.apps:
            people = self.appid_manager.get_people(appid)
            for i in range(self.duration):
                total_people[i] += people[i]

        # check data is exist
        if total_people[0] == 0:
            self.add_log("No this kind of data exist, please select the type again.")
        else:
            for appid in self.apps:
                # get data from appid
                people = self.appid_manager.get_people(appid)
                review = self.appid_manager.get_reviews(appid)
                price = self.appid_manager.get_price(appid)
                
                # data filtering formula : review * people * price / total people
                for i in range(self.duration):
                    total_price[i] += (review[i] * people[i] * price) / total_people[i]
                self.plot_manager.set_x_y(range(1,31), total_price)

        # send the signal of data filtering complete
        self.done.emit()

    def stop(self):
        self.wait()