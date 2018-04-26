# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\study_data\py_projects\frames\UI_frames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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
        icon.addPixmap(QtGui.QPixmap("titleicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        font = QtGui.QFont()
        font.setFamily("Arial")

        self.fileText = QTextBrowser(self.centralWidget)
        self.fileText.setGeometry(80, 100, 421, 28)

        # 设置文件显示栏
        font.setPointSize(7)
        self.fileText.setFont(font)
        self.fileText.setObjectName("fileText")
        self.LoadBtn = QPushButton(self.centralWidget)
        self.LoadBtn.setGeometry(510, 100, 31, 31)

        # 设置选择文件按钮
        font.setWeight(50)
        self.LoadBtn.setFont(font)
        self.LoadBtn.setAutoFillBackground(True)

        LoBtn= QIcon()
        LoBtn.addPixmap(QPixmap(":/icons/foldericon.ico"), QIcon.Normal, QIcon.Off)
        self.LoadBtn.setIcon(LoBtn)
        self.LoadBtn.setIconSize(QSize(40, 40))
        self.LoadBtn.setObjectName("LoadBtn")

        # 设置开始按钮
        self.staBtn = QPushButton(self.centralWidget)
        self.staBtn.setGeometry(200, 200, 81, 40)
        font.setPointSize(10)
        self.staBtn.setFont(font)
        self.staBtn.setObjectName("staBtn")

        # 设置打开图片按钮
        self.colBtn = QtWidgets.QPushButton(self.centralWidget)
        self.colBtn.setGeometry(QtCore.QRect(320, 230, 101, 40))
        self.colBtn.setFont(font)
        self.colBtn.setObjectName("colBtn")

        # 勾选设置图片大小选项
        self.RechBox = QtWidgets.QCheckBox(self.centralWidget)
        self.RechBox.setGeometry(QtCore.QRect(210, 120, 171, 27))   
        font.setPointSize(9)
        self.RechBox.setFont(font)
        self.RechBox.setObjectName("RechBox")

        #设置图片宽高
        self.wetLine = QtWidgets.QLineEdit(self.centralWidget)
        self.wetLine.setGeometry(QtCore.QRect(200, 170, 91, 29))
        self.wetLine.setFont(font)
        self.wetLine.setObjectName("wetLine")
        self.hetLine = QtWidgets.QLineEdit(self.centralWidget)
        self.hetLine.setGeometry(QtCore.QRect(320, 170, 91, 29))
        self.hetLine.setFont(font)
        self.hetLine.setObjectName("hetLine")
        # 乘号
        self.mulLal = QtWidgets.QLabel(self.centralWidget)
        self.mulLal.setGeometry(QtCore.QRect(300, 170, 16, 23))
        self.mulLal.setFont(font)
        self.mulLal.setObjectName("mulLal")
        
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "frames"))
        self.staBtn.setText(_translate("MainWindow", "Start"))
        self.colBtn.setText(_translate("MainWindow", "Pictures"))
        self.RechBox.setText(_translate("MainWindow", "Resize Picture"))
        self.mulLal.setText(_translate("MainWindow", "x"))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

