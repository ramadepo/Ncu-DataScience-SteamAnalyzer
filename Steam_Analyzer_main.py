import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
import time

import Steam_Analyzer_window

class Main(QMainWindow, Steam_Analyzer_window.Ui_MainWindow):
    def __init__(self):
        # initialize all essential object in GUI
        super().__init__()
        self.setupUi(self)

# program executed entry
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_window = Main()
    the_window.show()
    sys.exit(app.exec_())
