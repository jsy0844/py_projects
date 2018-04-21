# -*- coding: utf-8 -*-

"""
Module implementing Main_frames.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QFileDialog,QApplication

from Ui_UI_frames import Ui_MainWindow
import sys


class Main_frames(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Main_frames, self).__init__(parent)
        self.setupUi(self)
        self.action()

    def action(self):

        # 打开文件夹
        self.LoadBtn.clicked.connect(self.openFile)
        '''
        self.fileText.setText(self.filename)
        self.staBtn.clicked.connect(self.segm)
        self.colBtn.cliced.connect(self.openFra)
'''
    def openFile(self):
        QFileDialog.getOpenFileName(self, "Select Video", "/home")
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    frames = Main_frames()
    frames.show()
    sys.exit(app.exec_())
