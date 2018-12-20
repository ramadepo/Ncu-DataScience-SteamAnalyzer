import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QCheckBox

from Steam_Analyzer_Prediction_Manager import PredictionManager
import Steam_Analyzer_window

class Main(QMainWindow, Steam_Analyzer_window.Ui_MainWindow):
    def __init__(self):
        # initialize all essential object in GUI
        super().__init__()
        self.setupUi(self)
        self.single_manager = PredictionManager(self.tab_sin_price, 'sin')
        self.multi_manager = PredictionManager(self.tab_mul_price, 'mul')
    
    def get_price_sin(self):
        self.single_manager.work()

    def get_price_mul(self):
        self.multi_manager.work()

# program executed entry
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_window = Main()
    the_window.show()
    sys.exit(app.exec_())