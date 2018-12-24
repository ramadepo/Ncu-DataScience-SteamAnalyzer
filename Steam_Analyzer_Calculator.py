import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from PyQt5.QtCore import pyqtSignal, QObject

class Calculator(QObject):
    # signal of predict price for UI
    prediction_ok = pyqtSignal(float, float)
    log = pyqtSignal(str)
    
    def __init__(self, plot_manager, total_price, duration):
        QObject.__init__(self)
        self.plot_manager = plot_manager
        self.total_price = total_price
        self.duration = duration
        self.params = {'boosting_type': 'gbdt', 'max_depth' : -1, 'objective': 'regression', 'nthreads': 0}
        self.pf = PolynomialFeatures(degree=5, include_bias=False)
        self.regr = linear_model.LinearRegression()
        self.prediction_price = 0
        self.mse = 0
        self.prediction = []
    
    def calculate(self):
        self.train()
        self.log.emit("LGBM regression model training complete.\n")
        self.log.emit("Start to predict the price.\n")
        self.predict()
        self.plot_manager.plot_prediction(range(1, self.duration+2), self.prediction)
        

    # training stage
    def train(self):
        X = []
        for i in range(self.duration):
            X.append([i+1])
        y = self.total_price
        X_poly = self.pf.fit_transform(X)
        self.model = self.regr.fit(X_poly, y)
        self.mse = np.mean((self.model.predict(X_poly) - y) ** 2)
        self.prediction = list(self.model.predict(X_poly))

    # prediction stage
    def predict(self):
        X = [[self.duration+1]]
        X_poly = self.pf.fit_transform(X)
        self.prediction_price = self.model.predict(X_poly)
        self.prediction_ok.emit(self.prediction_price, self.mse)
        self.prediction.append(self.prediction_price)