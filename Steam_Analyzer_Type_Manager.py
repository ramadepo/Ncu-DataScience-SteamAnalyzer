from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QCheckBox
import pandas as pd

class AppTypeManager():
    def __init__(self):
        self.apptypes = pd.read_csv('data/applist_for_gametype.csv')
    
    def get_all_app_from_tags(self, tags):
        apps = []
        for app_types in self.apptypes.values:
            qualification = True
            for tag in tags:
                if tag not in app_types:
                    qualification = False
                    break
            if qualification:
                apps.append(app_types[0])
        return apps
    
