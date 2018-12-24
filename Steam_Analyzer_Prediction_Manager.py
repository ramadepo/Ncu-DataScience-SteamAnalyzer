from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextBrowser
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QLabel

from Steam_Analyzer_Type_Manager import AppTypeManager
from Steam_Analyzer_AppID_Manager import AppIDManager
from Steam_Analyzer_Calculator import Calculator
from Steam_Analyzer_Plot_Manager import PlotManager
from Steam_Analyzer_Thread import PlotThread, DataFilteringThread

class PredictionManager():
    def __init__(self, tab_widget, kind):
        self.tab_widget = tab_widget
        self.duration = 50
        self.now_date = '20181222'
        # kind is sin or mul
        self.kind = kind
        # manager for game type
        self.app_type_manager = AppTypeManager(self.kind)
        # manager for appid
        self.appid_manager = AppIDManager(self.now_date, self.duration)
        # manager for plotting
        self.plot_manager = PlotManager(self.tab_widget.findChild(QWidget, 'plot_' + self.kind + '_prediction'), 6, 6, 100)
        # log window object
        self.log_window = self.tab_widget.findChild(QTextBrowser, 'textBrowser_' + self.kind + '_log')
        # set slot and signal pair
        self.app_type_manager.log.connect(self.add_log)
        self.started = False

        self.tags = []
        self.apps = []

    # prepare the corresponding apps for types on UI
    def pre_work(self):
        self.tags = self.get_all_tags()
        print(self.tags) # remove #
        self.apps = self.app_type_manager.get_all_app_from_tags(self.tags)
        print(self.apps) # remove #

    # predict the price of game that with types on UI today from last 30 days evaluation by linear regression
    def work(self):
        self.started = True
        self.pre_work()
        self.set_plot_thread()
        self.set_data_filtering_thread()
        
    # set initial thread
    def set_plot_thread(self):
        self.plot_thread = PlotThread(self.plot_manager, self.tags)
        self.plot_thread.start()
    def set_data_filtering_thread(self):
        self.data_filtering_thread = DataFilteringThread(self.plot_manager, self.appid_manager, self.apps, self.duration)
        self.data_filtering_thread.done.connect(self.done)
        self.data_filtering_thread.log.connect(self.add_log)
        self.data_filtering_thread.progress.connect(self.update_progress)
        self.data_filtering_thread.total_people_num.connect(self.update_people)
        self.data_filtering_thread.total_price_ok.connect(self.set_calculator)
        self.data_filtering_thread.start()

    # data filtering done and set calculator with total price to start predict
    def set_calculator(self, total_price):
        self.calculator = Calculator(self.plot_manager, total_price, self.duration)
        self.calculator.prediction_ok.connect(self.update_price_mse)
        self.calculator.log.connect(self.add_log)
        self.calculator.calculate()
        
    # get tags from UI
    def get_all_tags(self):
        tags = []
        for child in self.tab_widget.children():
            if type(child) == QCheckBox:
                if child.isChecked():
                    tags.append(child.text())
        return tags

    # show log in log window
    def add_log(self, log):
        self.log_window.append(log)

    # receive the data filtering complete signal and turn off the thread
    def done(self):
        self.plot_thread.stop()
        self.data_filtering_thread.stop()
        self.started = False

    # update UI
    def update_progress(self, value):
        progress_bar = self.tab_widget.findChild(QProgressBar, 'progressBar_' + self.kind)
        progress_bar.setValue(value)
    def update_people(self, value):
        people_label = self.tab_widget.findChild(QLabel, 'label_' + self.kind + '_totalpeoplenum')
        people_label.setText(str(value))
    def update_price_mse(self, price, mse):
        price_label = self.tab_widget.findChild(QLabel, 'label_' + self.kind + '_price')
        price_label.setText(str(price))
        mse_label = self.tab_widget.findChild(QLabel, 'label_' + self.kind + '_msenum')
        mse_label.setText(str(mse))

    
