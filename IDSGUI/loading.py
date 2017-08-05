import sys
import random
#QT
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from load_ui import Ui_Dialog

#MATPLOT
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationBar
import numpy as np

class loading(QDialog):
    def __init__(self, parent=None):
        #super(main_window, self.__init__(parent))
        QWidget.__init__(self, parent)
        #Importing UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint | Qt.Dialog)
        #Setting up Initials
        # print("Constructor Called")
        # self.ui.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # gif=QMovie()
        # file = (QFileDialog.getOpenFileName())
        # gif.setFileName(file)
        # print(file)
        # print(QMovie.supportedFormats())
        # self.ui.label.setPixmap(QPixmap(file))
        # self.ui.label.setScaledContents(True)

        # self.ui.label.setMovie(gif)

        # gif.setCacheMode(QMovie.CacheAll)
        # gif.setSpeed(100)

        # self.ui.label.setPixmap(QPixmap("/home/pi/PycharmProjects/IDSGUI/assets/network.png"))
        # gif.start()
        # print(gif.frameCount())


