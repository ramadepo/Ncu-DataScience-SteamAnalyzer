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
    
    # button clicked event in single prediction tab
    def get_price_sin(self):
        if not self.single_manager.started:
            self.single_manager.work()
        else:
            self.single_manager.add_log('If you want to stop the program, please click the \"Stop\" button.\n')
    def stop_price_sin(self):
        self.single_manager.add_log("Manually stop the program.\n")
        self.single_manager.done()
    # button clicked event in multiple prediction tab
    def get_price_mul(self):
        if not self.multi_manager.started:
            self.multi_manager.work()
        else:
            self.multi_manager.add_log('If you want to stop the program, please click the \"Stop\" button.\n')
    def stop_price_mul(self):
        self.multi_manager.add_log("Manually stop the program.\n")
        self.multi_manager.done()

# program executed entry
if __name__ == "__main__":
    app = QApplication(sys.argv)
    the_window = Main()
    the_window.show()
    sys.exit(app.exec_())