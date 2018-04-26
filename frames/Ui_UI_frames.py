# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'I:\py_projects\frames\UI_frames.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


import icon_rc
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QWidget, QTextBrowser, QPushButton, QApplication, QMainWindow
from PyQt5.QtCore import QSize, QCoreApplication, QMetaObject




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        # 设置标题
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(621, 345)

        font = QFont()
        font.setFamily("Arial")
        font.setWeight(75)
        MainWindow.setFont(font)

        icon = QIcon()
        icon.addPixmap(QPixmap(":/icons/titleicon.ico"), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
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
        font.setWeight(50)
        self.staBtn.setFont(font)
        self.staBtn.setObjectName("staBtn")

        # 设置查看按钮
        self.colBtn = QPushButton(self.centralWidget)
        self.colBtn.setGeometry(330, 200, 91, 40)
        self.colBtn.setFont(font)
        self.colBtn.setObjectName("colBtn")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "frames"))
        self.staBtn.setText(_translate("MainWindow", "Start"))
        self.colBtn.setText(_translate("MainWindow", "Pictures"))
        self.colBtn.setEnabled(False)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

