# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filebrowser.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(425, 300)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 110, 401, 171))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.trainBrwse = QtGui.QPushButton(self.tab)
        self.trainBrwse.setGeometry(QtCore.QRect(290, 70, 99, 27))
        self.trainBrwse.setObjectName(_fromUtf8("trainBrwse"))
        self.trainingLine = QtGui.QLineEdit(self.tab)
        self.trainingLine.setGeometry(QtCore.QRect(10, 40, 381, 27))
        self.trainingLine.setObjectName(_fromUtf8("trainingLine"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 20, 351, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.TestFile = QtGui.QWidget()
        self.TestFile.setObjectName(_fromUtf8("TestFile"))
        self.testBrowse = QtGui.QPushButton(self.TestFile)
        self.testBrowse.setGeometry(QtCore.QRect(290, 70, 99, 27))
        self.testBrowse.setObjectName(_fromUtf8("testBrowse"))
        self.label_2 = QtGui.QLabel(self.TestFile)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 351, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.testingLine = QtGui.QLineEdit(self.TestFile)
        self.testingLine.setGeometry(QtCore.QRect(10, 40, 381, 27))
        self.testingLine.setObjectName(_fromUtf8("testingLine"))
        self.tabWidget.addTab(self.TestFile, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.testBrowse_2 = QtGui.QPushButton(self.tab_2)
        self.testBrowse_2.setGeometry(QtCore.QRect(290, 70, 99, 27))
        self.testBrowse_2.setObjectName(_fromUtf8("testBrowse_2"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 351, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.testingLine_2 = QtGui.QLineEdit(self.tab_2)
        self.testingLine_2.setGeometry(QtCore.QRect(10, 40, 381, 27))
        self.testingLine_2.setObjectName(_fromUtf8("testingLine_2"))
        self.okButton = QtGui.QPushButton(self.tab_2)
        self.okButton.setGeometry(QtCore.QRect(290, 100, 99, 27))
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(320, 20, 91, 91))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8(":/ui_start/png/filebrowse.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(_fromUtf8("border: 1px inset;\n"
""))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.trainBrwse.setText(_translate("Dialog", "Browse", None))
        self.label.setText(_translate("Dialog", "Please Select a Training Set", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Train Set", None))
        self.testBrowse.setText(_translate("Dialog", "Browse", None))
        self.label_2.setText(_translate("Dialog", "Please Select a Testing Set", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.TestFile), _translate("Dialog", "Test Set", None))
        self.testBrowse_2.setText(_translate("Dialog", "Browse", None))
        self.label_3.setText(_translate("Dialog", "Please Select Standard Labelled Test Set", None))
        self.okButton.setText(_translate("Dialog", "OK", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Standard Test Set", None))
        self.label_5.setText(_translate("Dialog", "Please Select Following Files", None))

import res_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

