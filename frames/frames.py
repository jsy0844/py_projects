# -*- coding: utf-8 -*-

"""
Module implementing Main_frames.
"""
from PyQt5.QtWidgets import QMainWindow, QFileDialog,QApplication, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from Ui_UI_frames import Ui_MainWindow
import sys
import os
import shutil


class Main_frames(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    fnamen = ""
    filepath = ""

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
        self.staBtn.clicked.connect(self.segm)
        self.colBtn.clicked.connect(self.openFra)
        self.reCkb.toggled.connect(self.showPicSize)

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, "Select Video", "","video(*.avi *.mov *.mpeg *.mpg *.wmv *.mp4 *.264 *.265 *.flv)")
        self.fileText.setText(fname[0])
        global fnamen
        fnamen = fname[0]
        #folname = QFileDialog.getExistingDirectory(self, "folder", "./")
        # print(folname)
        #fileinfo = QFileInfo(fname)
        #print(fname[0])
        #self.fileText.setText(fname)

    def segm(self):
        global fnamen, filepath#使用全局变量获取文件名加路径
        #print(fnamen)
        try:
            fnamen2 = fnamen.replace('/', '\\')#replace替换/和\, \需要转义
            filename = os.path.basename(fnamen2)#提前文件名
            filepath = os.path.dirname(fnamen2)#提取文件路径

            picpath = filepath + "\\frames"
            
            if os.path.exists(picpath):
                shutil.rmtree(picpath)
            os.chdir(filepath) 
                
            os.mkdir(r"./frames")
        except Exception:
            QMessageBox.warning(self, "No File", "No File was Selected!")
            return

        # 重新设置了图片大小
        if self.reCkb.isChecked():
            weight = self.weiLinE.text()
            height = self.heiLinE.text()

            if weight == "" or height == "":
                QMessageBox.warning(self, "parameter warning", "You need to enter the picture size!")
                return
            os.system("ffmpeg -i " + filename + " -s " + weight + "*" + height + " frames/out-%6d.jpg")

            if os.path.exists(".\\frames\\out-000001.jpg"):
                self.colBtn.setEnabled(True)
            else:
                QMessageBox.warning(self, "ffmpeg warning", "You need to add ffmpeg to your computer Environment Variables!")
        else:
            # 没设置图片大小
            os.system("ffmpeg -i " + filename + " frames/out-%6d.jpg")
            if os.path.exists(".\\frames\\out-000001.jpg"):
                self.colBtn.setEnabled(True)
            else:
                QMessageBox.warning(self, "ffmpeg warning", "You need to add ffmpeg to your computer Environment Variables!")


    def openFra(self):
        global filepath
        path = filepath + "\\frames"
        #fname = QFileDialog.getExistingDirectory(self, "Check pictures", filepath + "\\frames")
        os.startfile(path)
        '''
        new_path = r"open.bat"
        f = open(new_path, 'w')
        f.write("start /max " + filepath + "\\frames")
        f.close()
        #print(filepath)
        os.system("open.bat")
        '''
        
    def showPicSize(self, state):
        if self.reCkb.isChecked():
            self.weiLinE.setEnabled(True)
            self.weiLinE.setFocus()# 默认选择
            self.weiLinE.setPlaceholderText("1280")
            self.heiLinE.setEnabled(True)
            self.heiLinE.setPlaceholderText("720")
            self.mulLal.setEnabled(True)
            # self.reCkb.setColor(QPalette.WindowText, Qt.black)
        else:
            self.weiLinE.setEnabled(False)
            self.weiLinE.setPlaceholderText("")
            self.heiLinE.setEnabled(False)
            self.heiLinE.setPlaceholderText("")
            self.mulLal.setEnabled(False)
            # self.reCkb.setColor(QPalette.WindowText, Qt.gray)
'''
    def transWH(self, state):
        if state == Qt.Checked:
            weight = self.weiLinE.Text()
            height = self.heiLinE.Text()
        return weight, height'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    frames = Main_frames()
    frames.show()
    sys.exit(app.exec_())