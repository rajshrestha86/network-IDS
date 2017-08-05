import sys
import random
#QT
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from filebrowser_ui import Ui_Dialog
from loading import loading
from kdd_detection import ids
from res_window import res_window
#MATPLOT
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationBar
import numpy as np
res=0
class file_browser(QDialog):
    def __init__(self, parent=None):
        #super(main_window, self.__init__(parent))
        QWidget.__init__(self, parent)
        #Importing UI
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        #Setting up Initials
        # print("Constructor Called")
        self.connect(self.ui.trainBrwse, SIGNAL("clicked()"), lambda :self.train_select())
        self.connect(self.ui.testBrowse, SIGNAL("clicked()"), lambda: self.test_select())
        self.connect(self.ui.testBrowse_2, SIGNAL("clicked()"), lambda : self.test_std_select())
        self.connect(self.ui.okButton, SIGNAL("clicked()"), lambda: self.start())

    def train_select(self):
        self.ui.trainingLine.setText(QFileDialog.getOpenFileName())

    def test_select(self):
        self.ui.testingLine.setText(QFileDialog.getOpenFileName())

    def test_std_select(self):
        self.ui.testingLine_2.setText(QFileDialog.getOpenFileName())

    def start(self):
        print("Ok Button has been clicked.")
        train=self.ui.trainingLine.text()
        test=self.ui.testingLine.text()
        test_std_select=self.ui.testingLine_2.text()

        print("Test: ", train)
        if (train=="" or test=="" or test_std_select==""):
            print("Please select all the files.")
            msg=QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle("Error")
            msg.setText("You have not select all the datasets. Select all the valid datasets.")
            msg.exec()
            del msg
            return

        load_dialog = loading(self)

        load_win = loadthread(self, load_dialog)
        compute_thread = compute(self, train, test, test_std_select)


        load_dialog.connect(compute_thread, SIGNAL("finished()"), load_dialog, SLOT("close()"))
        self.connect(compute_thread, SIGNAL("finished()"), lambda: load_win.terminate())


        load_win.start()
        compute_thread.start()


        load_dialog.exec()

        # load_dialog.ui.progressBar.setV




        global res
        print(res)

        if res!= 0:
            message = QMessageBox(self)
            message.setIcon(QMessageBox.Critical)
            message.setWindowTitle("Error")
            message.setText(str(res))
            message.exec()
            res=0
            return
        self.close()
        result=res_window(self)
        result.show()














        # load_win.setPriority(QThread.NormalPriority)

        # self.hide()
        # self.connect(load_win, SIGNA)


class loadthread(QThread):
    def __init__(self, parent, dialog):
        super(loadthread, self).__init__(parent)
        self.load_dialog=dialog



    def run(self):
        i=3
        time=18

        while i>=0:
            self.sleep(1)
            self.load_dialog.ui.loading_anim.setText("..")
            self.load_dialog.ui.time.setText(str(time)+"s")
            # self.load_dialog.ui.progressBar.setValue(25)
            self.sleep(1)
            self.load_dialog.ui.loading_anim.setText("....")
            if time-2>=0:
                time-=2
            self.load_dialog.ui.time.setText(str(time)+"s")
            # self.load_dialog.ui.progressBar.setValue(50)
            self.sleep(1)
            self.load_dialog.ui.loading_anim.setText(".....")
            # self.load_dialog.ui.progressBar.setValue(75)
            self.sleep(1)
            if time-2 >= 0:
                time-=2
            self.load_dialog.ui.loading_anim.setText("......")
            self.load_dialog.ui.time.setText(str(time)+"s")
            # self.load_dialog.ui.progressBar.setValue(100)

            i+=1
            print("Threading....")

        print("Thread has stopped")



class compute(QThread):
    def __init__(self, parent, train, test, teststd):
        super(compute, self).__init__(parent)
        self.train=train
        self.test=test
        self.teststd=teststd




    def run(self):
        global res
        ids_obj = ids()
        res = ids_obj.main(self.train, self.test, self.teststd)

