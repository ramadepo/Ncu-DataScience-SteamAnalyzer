from PyQt5.QtWidgets import QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
class PlotManager(FigureCanvas):
    # initialize the object for plotting picture
    def __init__(self, parent, width, height, dpi):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        FigureCanvas.setSizePolicy(
            self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)
        self.x = []
        self.y = []
        self.changed = False
        self.init_plot()

    # first plot with nothing, just a line
    def init_plot(self):
        self.axes.clear()
        self.axes.set_title('Initialized')
        x = range(31)
        y = range(0, 1000, 33)
        self.axes.plot(x, y, color='red')
        self.draw()

    # clean the plot and set the title
    def subplot(self, tags):
        self.axes.clear()
        self.axes.set_title(tags)

    # plot the data filtering line
    def plot(self, tags):
        self.subplot(tags)
        self.axes.plot(self.x, self.y, color='red')
        self.draw()
        self.changed = False

    # set x and y coordinate
    def set_x_y(self, x, y):
        self.x = x
        self.y = y
        self.changed = True