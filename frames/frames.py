# -*- coding: utf-8 -*-

"""
Module implementing Main_frames.
"""
from PyQt5.QtWidgets import QMainWindow, QFileDialog,QApplication

from Ui_UI_frames import Ui_MainWindow
import sys
import os
import shutil


class Main_frames(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    fnamen = "ab"
    filepath = "12"

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

    def openFile(self):
        fname = QFileDialog.getOpenFileName(self, "Select Video", "./")
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
        # print(fnamen)
        fnamen2 = fnamen.replace('/', '\\')#replace替换/和\, \需要转义
        filename = os.path.basename(fnamen2)#提前文件名
        filepath = os.path.dirname(fnamen2)#提取文件路径

        picpath = filepath + "\\frames"
        
        if os.path.exists(picpath):
            shutil.rmtree(picpath)
        os.chdir(filepath) 
              
        os.mkdir(r"./frames/")

        os.system("ffmpeg -i " + filename + " frames/out-%6d.jpg")

        self.colBtn.setEnabled(True)

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
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    frames = Main_frames()
    frames.show()
    sys.exit(app.exec_())