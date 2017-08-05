import sys
from mainwindow import main_window
from filebrowser import  file_browser
from PyQt4 import QtGui


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    a=main_window()
    a.show()
    sys.exit(app.exec_())
    del app



