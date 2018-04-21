# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\study data\pyqt5_projects\frames\UI_frames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(686, 466)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.fileText = QtWidgets.QTextBrowser(self.centralWidget)
        self.fileText.setGeometry(QtCore.QRect(320, 110, 181, 41))
        self.fileText.setObjectName("fileText")
        self.LoadBtn = QtWidgets.QPushButton(self.centralWidget)
        self.LoadBtn.setGeometry(QtCore.QRect(170, 110, 131, 40))
        self.LoadBtn.setObjectName("LoadBtn")
        self.staBtn = QtWidgets.QPushButton(self.centralWidget)
        self.staBtn.setGeometry(QtCore.QRect(170, 200, 131, 40))
        self.staBtn.setObjectName("staBtn")
        self.colBtn = QtWidgets.QPushButton(self.centralWidget)
        self.colBtn.setGeometry(QtCore.QRect(320, 200, 171, 40))
        self.colBtn.setObjectName("colBtn")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.LoadBtn.setText(_translate("MainWindow", "Load"))
        self.staBtn.setText(_translate("MainWindow", "Start"))
        self.colBtn.setText(_translate("MainWindow", "collect pictures"))
        self.colBtn.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

