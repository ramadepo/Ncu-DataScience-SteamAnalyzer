from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QCheckBox
import pandas as pd

class AppTypeManager(QObject):
    # signal for log
    log = pyqtSignal(str)
    def __init__(self, kind):
        QObject.__init__(self)
        # kind is sin or mul
        self.kind = kind
        # load file
        self.apptypes = pd.read_csv('data/applist_for_gametype.csv')
        self.appsupport = pd.read_csv('data/applist_for_support.csv')
    
    def get_all_app_from_tags(self, tags):
        apps = []
        # check the qualification of types on UI
        for app_types in self.apptypes.values:
            qualification = True
            if len(tags) == 0:
                self.log.emit('Please choose the type of game')
                break
            for tag in tags:
                if tag not in app_types:
                    qualification = False
                    break
            if qualification:
                appid = app_types[0]
                # check the data is exist
                support_list = self.appsupport[self.appsupport['AppID'] == appid].values
                if len(support_list) != 0:
                    # check now is single or multiple tab and store corresponding data
                    if self.kind == 'sin':
                        if 'Online Multi-Player' not in support_list[0][2:]:
                            apps.append(appid)
                    elif self.kind == 'mul':
                        if 'Online Multi-Player' in support_list[0][2:]:
                            apps.append(appid)
        return apps
    
