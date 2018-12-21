# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SteamAnalyzer.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1200, 930)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 930))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 930))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: rgb(203, 235, 253);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1201, 931))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_sin_price = QtWidgets.QWidget()
        self.tab_sin_price.setEnabled(True)
        self.tab_sin_price.setObjectName("tab_sin_price")
        self.plot_sin_prediction = QtWidgets.QWidget(self.tab_sin_price)
        self.plot_sin_prediction.setGeometry(QtCore.QRect(10, 290, 600, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.plot_sin_prediction.setFont(font)
        self.plot_sin_prediction.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot_sin_prediction.setObjectName("plot_sin_prediction")
        self.button_sin_prediction = QtWidgets.QPushButton(self.tab_sin_price)
        self.button_sin_prediction.setGeometry(QtCore.QRect(990, 140, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.button_sin_prediction.setFont(font)
        self.button_sin_prediction.setObjectName("button_sin_prediction")
        self.checkBox_sin_action = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_action.setGeometry(QtCore.QRect(30, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_action.setFont(font)
        self.checkBox_sin_action.setObjectName("checkBox_sin_action")
        self.checkBox_sin_adventure = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_adventure.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_adventure.setFont(font)
        self.checkBox_sin_adventure.setObjectName("checkBox_sin_adventure")
        self.checkBox_sin_animationandmodeling = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_animationandmodeling.setGeometry(QtCore.QRect(30, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_animationandmodeling.setFont(font)
        self.checkBox_sin_animationandmodeling.setObjectName("checkBox_sin_animationandmodeling")
        self.checkBox_sin_indie = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_indie.setGeometry(QtCore.QRect(510, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_indie.setFont(font)
        self.checkBox_sin_indie.setObjectName("checkBox_sin_indie")
        self.checkBox_sin_earlyaccess = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_earlyaccess.setGeometry(QtCore.QRect(270, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_earlyaccess.setFont(font)
        self.checkBox_sin_earlyaccess.setObjectName("checkBox_sin_earlyaccess")
        self.checkBox_sin_rpg = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_rpg.setGeometry(QtCore.QRect(510, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_rpg.setFont(font)
        self.checkBox_sin_rpg.setObjectName("checkBox_sin_rpg")
        self.checkBox_sin_freetoplay = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_freetoplay.setGeometry(QtCore.QRect(270, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_freetoplay.setFont(font)
        self.checkBox_sin_freetoplay.setObjectName("checkBox_sin_freetoplay")
        self.checkBox_sin_massivelymultiplayer = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_massivelymultiplayer.setGeometry(QtCore.QRect(510, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_massivelymultiplayer.setFont(font)
        self.checkBox_sin_massivelymultiplayer.setObjectName("checkBox_sin_massivelymultiplayer")
        self.checkBox_sin_strategy = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_strategy.setGeometry(QtCore.QRect(750, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_strategy.setFont(font)
        self.checkBox_sin_strategy.setObjectName("checkBox_sin_strategy")
        self.checkBox_sin_casual = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_casual.setGeometry(QtCore.QRect(30, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_casual.setFont(font)
        self.checkBox_sin_casual.setObjectName("checkBox_sin_casual")
        self.checkBox_sin_simulation = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_simulation.setGeometry(QtCore.QRect(750, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_simulation.setFont(font)
        self.checkBox_sin_simulation.setObjectName("checkBox_sin_simulation")
        self.checkBox_sin_racing = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_racing.setGeometry(QtCore.QRect(510, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_racing.setFont(font)
        self.checkBox_sin_racing.setObjectName("checkBox_sin_racing")
        self.checkBox_sin_sports = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_sports.setGeometry(QtCore.QRect(750, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_sports.setFont(font)
        self.checkBox_sin_sports.setObjectName("checkBox_sin_sports")
        self.checkBox_sin_utilities = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_utilities.setGeometry(QtCore.QRect(750, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_utilities.setFont(font)
        self.checkBox_sin_utilities.setObjectName("checkBox_sin_utilities")
        self.checkBox_sin_vedioproduction = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_vedioproduction.setGeometry(QtCore.QRect(990, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_vedioproduction.setFont(font)
        self.checkBox_sin_vedioproduction.setObjectName("checkBox_sin_vedioproduction")
        self.checkBox_sin_designandillustration = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_designandillustration.setGeometry(QtCore.QRect(270, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_designandillustration.setFont(font)
        self.checkBox_sin_designandillustration.setObjectName("checkBox_sin_designandillustration")
        self.checkBox_sin_photoediting = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_photoediting.setGeometry(QtCore.QRect(510, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_photoediting.setFont(font)
        self.checkBox_sin_photoediting.setObjectName("checkBox_sin_photoediting")
        self.checkBox_sin_webpublishing = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_webpublishing.setGeometry(QtCore.QRect(990, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_webpublishing.setFont(font)
        self.checkBox_sin_webpublishing.setObjectName("checkBox_sin_webpublishing")
        self.checkBox_sin_education = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_education.setGeometry(QtCore.QRect(270, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_education.setFont(font)
        self.checkBox_sin_education.setObjectName("checkBox_sin_education")
        self.checkBox_sin_softwaretraining = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_softwaretraining.setGeometry(QtCore.QRect(750, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_softwaretraining.setFont(font)
        self.checkBox_sin_softwaretraining.setObjectName("checkBox_sin_softwaretraining")
        self.checkBox_sin_audioproduction = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_audioproduction.setGeometry(QtCore.QRect(30, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_audioproduction.setFont(font)
        self.checkBox_sin_audioproduction.setObjectName("checkBox_sin_audioproduction")
        self.checkBox_sin_gamedevelopment = QtWidgets.QCheckBox(self.tab_sin_price)
        self.checkBox_sin_gamedevelopment.setGeometry(QtCore.QRect(270, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_sin_gamedevelopment.setFont(font)
        self.checkBox_sin_gamedevelopment.setObjectName("checkBox_sin_gamedevelopment")
        self.progressBar_sin = QtWidgets.QProgressBar(self.tab_sin_price)
        self.progressBar_sin.setGeometry(QtCore.QRect(630, 290, 551, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.progressBar_sin.setFont(font)
        self.progressBar_sin.setProperty("value", 0)
        self.progressBar_sin.setObjectName("progressBar_sin")
        self.label_sin_priceprediction = QtWidgets.QLabel(self.tab_sin_price)
        self.label_sin_priceprediction.setGeometry(QtCore.QRect(630, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_sin_priceprediction.setFont(font)
        self.label_sin_priceprediction.setObjectName("label_sin_priceprediction")
        self.label_sin_price = QtWidgets.QLabel(self.tab_sin_price)
        self.label_sin_price.setGeometry(QtCore.QRect(810, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_sin_price.setFont(font)
        self.label_sin_price.setObjectName("label_sin_price")
        self.textBrowser_sin_log = QtWidgets.QTextBrowser(self.tab_sin_price)
        self.textBrowser_sin_log.setGeometry(QtCore.QRect(630, 691, 551, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_sin_log.setFont(font)
        self.textBrowser_sin_log.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);")
        self.textBrowser_sin_log.setObjectName("textBrowser_sin_log")
        self.tabWidget.addTab(self.tab_sin_price, "")
        self.tab_mul_price = QtWidgets.QWidget()
        self.tab_mul_price.setObjectName("tab_mul_price")
        self.plot_mul_prediction = QtWidgets.QWidget(self.tab_mul_price)
        self.plot_mul_prediction.setGeometry(QtCore.QRect(10, 290, 600, 600))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.plot_mul_prediction.setFont(font)
        self.plot_mul_prediction.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.plot_mul_prediction.setObjectName("plot_mul_prediction")
        self.checkBox_mul_designandillustration = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_designandillustration.setGeometry(QtCore.QRect(270, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_designandillustration.setFont(font)
        self.checkBox_mul_designandillustration.setObjectName("checkBox_mul_designandillustration")
        self.checkBox_mul_earlyaccess = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_earlyaccess.setGeometry(QtCore.QRect(270, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_earlyaccess.setFont(font)
        self.checkBox_mul_earlyaccess.setObjectName("checkBox_mul_earlyaccess")
        self.checkBox_mul_indie = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_indie.setGeometry(QtCore.QRect(510, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_indie.setFont(font)
        self.checkBox_mul_indie.setObjectName("checkBox_mul_indie")
        self.checkBox_mul_sports = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_sports.setGeometry(QtCore.QRect(750, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_sports.setFont(font)
        self.checkBox_mul_sports.setObjectName("checkBox_mul_sports")
        self.checkBox_mul_action = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_action.setGeometry(QtCore.QRect(30, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_action.setFont(font)
        self.checkBox_mul_action.setObjectName("checkBox_mul_action")
        self.checkBox_mul_simulation = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_simulation.setGeometry(QtCore.QRect(750, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_simulation.setFont(font)
        self.checkBox_mul_simulation.setObjectName("checkBox_mul_simulation")
        self.checkBox_mul_freetoplay = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_freetoplay.setGeometry(QtCore.QRect(270, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_freetoplay.setFont(font)
        self.checkBox_mul_freetoplay.setObjectName("checkBox_mul_freetoplay")
        self.checkBox_mul_webpublishing = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_webpublishing.setGeometry(QtCore.QRect(990, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_webpublishing.setFont(font)
        self.checkBox_mul_webpublishing.setObjectName("checkBox_mul_webpublishing")
        self.button_mul_prediction = QtWidgets.QPushButton(self.tab_mul_price)
        self.button_mul_prediction.setGeometry(QtCore.QRect(990, 140, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.button_mul_prediction.setFont(font)
        self.button_mul_prediction.setObjectName("button_mul_prediction")
        self.checkBox_mul_education = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_education.setGeometry(QtCore.QRect(270, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_education.setFont(font)
        self.checkBox_mul_education.setObjectName("checkBox_mul_education")
        self.checkBox_mul_softwaretraining = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_softwaretraining.setGeometry(QtCore.QRect(750, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_softwaretraining.setFont(font)
        self.checkBox_mul_softwaretraining.setObjectName("checkBox_mul_softwaretraining")
        self.checkBox_mul_gamedevelopment = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_gamedevelopment.setGeometry(QtCore.QRect(270, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_gamedevelopment.setFont(font)
        self.checkBox_mul_gamedevelopment.setObjectName("checkBox_mul_gamedevelopment")
        self.checkBox_mul_casual = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_casual.setGeometry(QtCore.QRect(30, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_casual.setFont(font)
        self.checkBox_mul_casual.setObjectName("checkBox_mul_casual")
        self.checkBox_mul_audioproduction = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_audioproduction.setGeometry(QtCore.QRect(30, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_audioproduction.setFont(font)
        self.checkBox_mul_audioproduction.setObjectName("checkBox_mul_audioproduction")
        self.checkBox_mul_vedioproduction = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_vedioproduction.setGeometry(QtCore.QRect(990, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_vedioproduction.setFont(font)
        self.checkBox_mul_vedioproduction.setObjectName("checkBox_mul_vedioproduction")
        self.checkBox_mul_photoediting = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_photoediting.setGeometry(QtCore.QRect(510, 100, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_photoediting.setFont(font)
        self.checkBox_mul_photoediting.setObjectName("checkBox_mul_photoediting")
        self.checkBox_mul_strategy = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_strategy.setGeometry(QtCore.QRect(750, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_strategy.setFont(font)
        self.checkBox_mul_strategy.setObjectName("checkBox_mul_strategy")
        self.checkBox_mul_racing = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_racing.setGeometry(QtCore.QRect(510, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_racing.setFont(font)
        self.checkBox_mul_racing.setObjectName("checkBox_mul_racing")
        self.checkBox_mul_animationandmodeling = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_animationandmodeling.setGeometry(QtCore.QRect(30, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_animationandmodeling.setFont(font)
        self.checkBox_mul_animationandmodeling.setObjectName("checkBox_mul_animationandmodeling")
        self.checkBox_mul_adventure = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_adventure.setGeometry(QtCore.QRect(30, 60, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_adventure.setFont(font)
        self.checkBox_mul_adventure.setObjectName("checkBox_mul_adventure")
        self.checkBox_mul_rpg = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_rpg.setGeometry(QtCore.QRect(510, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_rpg.setFont(font)
        self.checkBox_mul_rpg.setObjectName("checkBox_mul_rpg")
        self.checkBox_mul_massivelymultiplayer = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_massivelymultiplayer.setGeometry(QtCore.QRect(510, 60, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_massivelymultiplayer.setFont(font)
        self.checkBox_mul_massivelymultiplayer.setObjectName("checkBox_mul_massivelymultiplayer")
        self.checkBox_mul_utilities = QtWidgets.QCheckBox(self.tab_mul_price)
        self.checkBox_mul_utilities.setGeometry(QtCore.QRect(750, 180, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.checkBox_mul_utilities.setFont(font)
        self.checkBox_mul_utilities.setObjectName("checkBox_mul_utilities")
        self.progressBar_mul = QtWidgets.QProgressBar(self.tab_mul_price)
        self.progressBar_mul.setGeometry(QtCore.QRect(630, 290, 551, 23))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.progressBar_mul.setFont(font)
        self.progressBar_mul.setProperty("value", 0)
        self.progressBar_mul.setObjectName("progressBar_mul")
        self.label_mul_priceprediction = QtWidgets.QLabel(self.tab_mul_price)
        self.label_mul_priceprediction.setGeometry(QtCore.QRect(630, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_mul_priceprediction.setFont(font)
        self.label_mul_priceprediction.setObjectName("label_mul_priceprediction")
        self.label_mul_price = QtWidgets.QLabel(self.tab_mul_price)
        self.label_mul_price.setGeometry(QtCore.QRect(810, 330, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_mul_price.setFont(font)
        self.label_mul_price.setObjectName("label_mul_price")
        self.textBrowser_mul_log = QtWidgets.QTextBrowser(self.tab_mul_price)
        self.textBrowser_mul_log.setGeometry(QtCore.QRect(630, 690, 551, 201))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.textBrowser_mul_log.setFont(font)
        self.textBrowser_mul_log.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(0, 255, 0);")
        self.textBrowser_mul_log.setObjectName("textBrowser_mul_log")
        self.tabWidget.addTab(self.tab_mul_price, "")
        self.tab_sin_top = QtWidgets.QWidget()
        self.tab_sin_top.setObjectName("tab_sin_top")
        self.tabWidget.addTab(self.tab_sin_top, "")
        self.tab_mul_top = QtWidgets.QWidget()
        self.tab_mul_top.setObjectName("tab_mul_top")
        self.tabWidget.addTab(self.tab_mul_top, "")
        self.tab_help = QtWidgets.QWidget()
        self.tab_help.setObjectName("tab_help")
        self.tabWidget.addTab(self.tab_help, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.button_sin_prediction.clicked.connect(MainWindow.get_price_sin)
        self.button_mul_prediction.clicked.connect(MainWindow.get_price_mul)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Steam Analyzer"))
        self.button_sin_prediction.setText(_translate("MainWindow", "Get Price !!!"))
        self.checkBox_sin_action.setText(_translate("MainWindow", "Action"))
        self.checkBox_sin_adventure.setText(_translate("MainWindow", "Adventure"))
        self.checkBox_sin_animationandmodeling.setText(_translate("MainWindow", "Animation & Modeling"))
        self.checkBox_sin_indie.setText(_translate("MainWindow", "Indie"))
        self.checkBox_sin_earlyaccess.setText(_translate("MainWindow", "Early Access"))
        self.checkBox_sin_rpg.setText(_translate("MainWindow", "RPG"))
        self.checkBox_sin_freetoplay.setText(_translate("MainWindow", "Free to Play"))
        self.checkBox_sin_massivelymultiplayer.setText(_translate("MainWindow", "Massively Multiplayer"))
        self.checkBox_sin_strategy.setText(_translate("MainWindow", "Strategy"))
        self.checkBox_sin_casual.setText(_translate("MainWindow", "Casual"))
        self.checkBox_sin_simulation.setText(_translate("MainWindow", "Simulation"))
        self.checkBox_sin_racing.setText(_translate("MainWindow", "Racing"))
        self.checkBox_sin_sports.setText(_translate("MainWindow", "Sports"))
        self.checkBox_sin_utilities.setText(_translate("MainWindow", "Utilities"))
        self.checkBox_sin_vedioproduction.setText(_translate("MainWindow", "Vedio Production"))
        self.checkBox_sin_designandillustration.setText(_translate("MainWindow", "Design & Illustration"))
        self.checkBox_sin_photoediting.setText(_translate("MainWindow", "Photo Editing"))
        self.checkBox_sin_webpublishing.setText(_translate("MainWindow", "Web Publishing"))
        self.checkBox_sin_education.setText(_translate("MainWindow", "Education"))
        self.checkBox_sin_softwaretraining.setText(_translate("MainWindow", "Software Training"))
        self.checkBox_sin_audioproduction.setText(_translate("MainWindow", "Audio Production"))
        self.checkBox_sin_gamedevelopment.setText(_translate("MainWindow", "Game Development"))
        self.label_sin_priceprediction.setText(_translate("MainWindow", "Price Prediction : "))
        self.label_sin_price.setText(_translate("MainWindow", "0"))
        self.textBrowser_sin_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here Is Log Window</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sin_price), _translate("MainWindow", "Predictions(Single)"))
        self.checkBox_mul_designandillustration.setText(_translate("MainWindow", "Design & Illustration"))
        self.checkBox_mul_earlyaccess.setText(_translate("MainWindow", "Early Access"))
        self.checkBox_mul_indie.setText(_translate("MainWindow", "Indie"))
        self.checkBox_mul_sports.setText(_translate("MainWindow", "Sports"))
        self.checkBox_mul_action.setText(_translate("MainWindow", "Action"))
        self.checkBox_mul_simulation.setText(_translate("MainWindow", "Simulation"))
        self.checkBox_mul_freetoplay.setText(_translate("MainWindow", "Free to Play"))
        self.checkBox_mul_webpublishing.setText(_translate("MainWindow", "Web Publishing"))
        self.button_mul_prediction.setText(_translate("MainWindow", "Get Price !!!"))
        self.checkBox_mul_education.setText(_translate("MainWindow", "Education"))
        self.checkBox_mul_softwaretraining.setText(_translate("MainWindow", "Software Training"))
        self.checkBox_mul_gamedevelopment.setText(_translate("MainWindow", "Game Development"))
        self.checkBox_mul_casual.setText(_translate("MainWindow", "Casual"))
        self.checkBox_mul_audioproduction.setText(_translate("MainWindow", "Audio Production"))
        self.checkBox_mul_vedioproduction.setText(_translate("MainWindow", "Vedio Production"))
        self.checkBox_mul_photoediting.setText(_translate("MainWindow", "Photo Editing"))
        self.checkBox_mul_strategy.setText(_translate("MainWindow", "Strategy"))
        self.checkBox_mul_racing.setText(_translate("MainWindow", "Racing"))
        self.checkBox_mul_animationandmodeling.setText(_translate("MainWindow", "Animation & Modeling"))
        self.checkBox_mul_adventure.setText(_translate("MainWindow", "Adventure"))
        self.checkBox_mul_rpg.setText(_translate("MainWindow", "RPG"))
        self.checkBox_mul_massivelymultiplayer.setText(_translate("MainWindow", "Massively Multiplayer"))
        self.checkBox_mul_utilities.setText(_translate("MainWindow", "Utilities"))
        self.label_mul_priceprediction.setText(_translate("MainWindow", "Price Prediction : "))
        self.label_mul_price.setText(_translate("MainWindow", "0"))
        self.textBrowser_mul_log.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Here Is Log Window</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mul_price), _translate("MainWindow", "Predictions(Multi)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sin_top), _translate("MainWindow", "Top Types(Single)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_mul_top), _translate("MainWindow", "Top Types(Multi)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_help), _translate("MainWindow", "Intro"))

