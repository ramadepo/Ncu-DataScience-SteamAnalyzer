from PyQt5.QtCore import QThread,pyqtSignal
import numpy as np
import time

class PlotThread(QThread):
    def __init__(self, plot_manager, tags):
        QThread.__init__(self)
        self.plot_manager = plot_manager
        self.tags = tags
        self.active = True
        
    def run(self):
        # check the thread is alive or not
        while self.active:
            if self.plot_manager.changed:
                self.plot_manager.plot(self.tags)
            time.sleep(0.0000000000000000000000000000000000000000000001)

    def stop(self):
        self.active = False
        self.wait()

class DataFilteringThread(QThread):
    log = pyqtSignal(str)
    done = pyqtSignal()
    progress = pyqtSignal(int)
    total_people_num = pyqtSignal(float)
    total_price_ok = pyqtSignal(list)
    def __init__(self, plot_manager, appid_manager, apps, duration):
        QThread.__init__(self)
        self.plot_manager = plot_manager
        self.appid_manager = appid_manager
        self.apps = apps
        self.duration = duration
        self.active = True

    def run(self):
        total_people = [0] * self.duration
        total_price = [0.0] * self.duration
        time_count = 0

        for appid in self.apps:
            # check the thread is alive or not
            if self.active:
                # get data from appid
                people = self.appid_manager.get_people(appid)
                review = self.appid_manager.get_reviews(appid)
                price = self.appid_manager.get_price(appid)
                # data filtering formula : review * people * price / total people
                for i in range(self.duration):
                    total_price[i] += review[i] * people[i] * price
                    total_people[i] += people[i]
                time_count += 1
                # update UI
                self.progress.emit(int(time_count * 100 /len(self.apps)))
                self.total_people_num.emit(float(np.sum(total_people)/self.duration))
                if time_count%100 == 0:
                    self.plot_manager.set_x_y(range(1,self.duration+1), total_price)


            
        # check data is exist
        if total_people[0] == 0:
            self.log.emit('No this kind of data exist, please select the type again.\n')
            self.done.emit()
        else:
            # calculate total average price
            for i in range(self.duration):
                total_price[i] /= total_people[i]
            self.plot_manager.set_x_y(range(1,self.duration+1), total_price)
            # send the signal of data filtering complete
            if self.active:
                self.log.emit('Data filtering complete.\n')
                self.done.emit()
                self.total_price_ok.emit(total_price)

    def stop(self):
        self.active = False
        self.wait()