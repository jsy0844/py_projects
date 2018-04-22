# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:\py_projects\frames\UI_frames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import icon_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 345)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/titleicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.fileText = QtWidgets.QTextBrowser(self.centralWidget)
        self.fileText.setGeometry(QtCore.QRect(80, 100, 421, 28))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.fileText.setFont(font)
        self.fileText.setObjectName("fileText")
        self.LoadBtn = QtWidgets.QPushButton(self.centralWidget)
        self.LoadBtn.setGeometry(QtCore.QRect(510, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        font.setWeight(50)
        self.LoadBtn.setFont(font)
        self.LoadBtn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.LoadBtn.setAutoFillBackground(True)
        self.LoadBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/foldericon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.LoadBtn.setIcon(icon1)
        self.LoadBtn.setIconSize(QtCore.QSize(40, 40))
        self.LoadBtn.setObjectName("LoadBtn")
        self.staBtn = QtWidgets.QPushButton(self.centralWidget)
        self.staBtn.setGeometry(QtCore.QRect(200, 200, 81, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.staBtn.setFont(font)
        self.staBtn.setObjectName("staBtn")
        self.colBtn = QtWidgets.QPushButton(self.centralWidget)
        self.colBtn.setGeometry(QtCore.QRect(340, 200, 81, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.colBtn.setFont(font)
        self.colBtn.setObjectName("colBtn")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "frames"))
        self.staBtn.setText(_translate("MainWindow", "Start"))
        self.colBtn.setText(_translate("MainWindow", "Pictures"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

