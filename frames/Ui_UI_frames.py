# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\study_data\py_projects\frames\UI_frames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
import icon_rc
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QTextBrowser, QPushButton, QApplication, QMainWindow, QCheckBox, QLineEdit, QLabel
from PyQt5.QtCore import QSize, QCoreApplication, QMetaObject


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        # 设置标题
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 345)

        font = QFont()
        font.setFamily("Arial")
        font.setWeight(75)
        MainWindow.setFont(font)

        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/titleicon.ico"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")

        # 设置文件显示栏
        self.fileText = QTextBrowser(self.centralWidget)
        self.fileText.setGeometry(70, 60, 421, 31)
        font.setPointSize(7)
        self.fileText.setFont(font)
        self.fileText.setObjectName("fileText")

        # 设置选择文件按钮
        self.LoadBtn = QPushButton(self.centralWidget)
        self.LoadBtn.setGeometry(500, 60, 33, 33)     
        self.LoadBtn.setAutoFillBackground(True)
        LoBtn= QIcon()
        LoBtn.addPixmap(QPixmap(":/icons/foldericon.ico"), QIcon.Normal, QIcon.Off)
        self.LoadBtn.setIcon(LoBtn)
        self.LoadBtn.setIconSize(QSize(43, 43))
        self.LoadBtn.setObjectName("LoadBtn")
        self.LoadBtn.setFlat(True)

        # 设置开始按钮
        self.staBtn = QPushButton(self.centralWidget)
        self.staBtn.setGeometry(190, 230, 81, 40)
        font.setWeight(50)
        font.setPointSize(10)
        self.staBtn.setFont(font)
        self.staBtn.setObjectName("staBtn")

        # 设置查看按钮
        self.colBtn = QPushButton(self.centralWidget)
        self.colBtn.setGeometry(310, 230, 101, 40)
        self.colBtn.setFont(font)
        self.colBtn.setObjectName("colBtn")
        self.colBtn.setEnabled(False)

        # 图片大小选框
        self.reCkb = QCheckBox(self.centralWidget)
        self.reCkb.setGeometry(190, 120, 171, 27)
        font.setPointSize(9)
        self.reCkb.setFont(font)
        self.reCkb.setObjectName("reCkb")

        # 设置图片宽高，x号
        self.weiLinE = QLineEdit(self.centralWidget)
        self.weiLinE.setEnabled(False)
        self.weiLinE.setGeometry(190, 170, 81, 29)
        self.weiLinE.setFont(font)
        self.weiLinE.setObjectName("weiLinE")
        
        self.heiLinE = QLineEdit(self.centralWidget)
        self.heiLinE.setEnabled(False)
        self.heiLinE.setGeometry(310, 170, 81, 29)
        self.heiLinE.setFont(font)
        self.heiLinE.setObjectName("heiLinE")
        
        self.mulLal = QLabel(self.centralWidget)
        self.mulLal.setGeometry(285, 170, 16, 23)
        self.mulLal.setFont(font)
        self.mulLal.setObjectName("mulLal")
        self.mulLal.setEnabled(False)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "frames"))
        self.staBtn.setText(_translate("MainWindow", "Start"))
        self.colBtn.setText(_translate("MainWindow", "Pictures"))
        self.reCkb.setText(_translate("MainWindow", "Resize picture"))
        self.mulLal.setText(_translate("MainWindow", "x"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

