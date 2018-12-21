from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QCheckBox

from Steam_Analyzer_Type_Manager import AppTypeManager
from Steam_Analyzer_AppID_Manager import AppIDManager

class PredictionManager():
    def __init__(self, tab_widget, kind):
        self.tab_widget = tab_widget
        # kind is sin or mul
        self.kind = kind
        # manager for game type
        self.app_type_manager = AppTypeManager(self.kind)
        # manager for appid
        self.appid_manager = AppIDManager('20181215', 30)

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
        self.pre_work()

        
    # get tags from UI
    def get_all_tags(self):
        tags = []
        for child in self.tab_widget.children():
            if type(child) == QCheckBox:
                if child.isChecked():
                    tags.append(child.text())
        return tags