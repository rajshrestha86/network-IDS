import sys
import random
#QT
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from mainwindow_ui import Ui_MainWindow
from filebrowser import file_browser
#MATPLOT
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationBar
import numpy as np

class main_window(QMainWindow):
    def __init__(self, parent=None):
        #super(main_window, self.__init__(parent))
        QWidget.__init__(self, parent)
        #Importing UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #Setting up Initials
        # print("Constructor Called")
        self.setFixedSize(1024,640)
        self.ui.pushButton.setFocusPolicy(Qt.NoFocus)
        self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        self.setWindowTitle("NIDS")
        self.connect( self.ui.pushButton, SIGNAL("clicked()"), lambda: self.clicked())
        # self.ui.pushButton.setChecked(True)
        # self.ui.pushButton_3.setChecked(True)
        # self.ui.pushButton_2.setChecked(False)


    def init(self):
        print("Hello")



    def clicked(self):
        print("Clicked")

        file_win=file_browser()
        self.close()
        file_win.exec()




