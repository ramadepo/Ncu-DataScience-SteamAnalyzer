from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
class PlotManager(FigureCanvas):
    def __init__(self, parent, width, height, dpi):
        # initialize the object for plotting picture
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.init_plot()
    def init_plot(self):
        self.axes.clear()
        self.axes.set_title('Initialized')
        self.axes.set_xlim(0, 30)
        self.axes.set_ylim(0, 1000)
        x = range(31)
        y = range(0, 1000, 33)
        self.axes.plot(x, y, color='red')
        self.draw()