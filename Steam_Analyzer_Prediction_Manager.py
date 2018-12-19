from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QCheckBox

from Steam_Analyzer_Type_Manager import AppTypeManager

class PredictionManager():
    def __init__(self, tab_widget):
        self.tab_widget = tab_widget
        self.app_type_manager = AppTypeManager()
        self.tags = []
        self.apps = []

    def pre_work(self):
        self.tags = self.get_all_tags()
        print(self.tags) # remove #
        self.apps = self.app_type_manager.get_all_app_from_tags(self.tags)
        print(self.apps) # remove #

    def work(self):
        self.pre_work()
        

    def get_all_tags(self):
        tags = []
        for child in self.tab_widget.children():
            if type(child) == QCheckBox:
                if child.isChecked():
                    tags.append(child.text())
        return tags