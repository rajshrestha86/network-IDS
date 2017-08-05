import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from res_window_ui import Ui_MainWindow
# from filebrowser import file_browser


from pylab import *
from matplotlib.backends.backend_qt4agg import (
	FigureCanvasQTAgg as FigureCanvas,
	NavigationToolbar2QT as NavigationToolbar)

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt



class res_window(QMainWindow):
    def __init__(self, parent=None):
        #super(main_window, self.__init__(parent))
        QWidget.__init__(self, parent)
        #Importing UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setFixedSize(1336, 768)
        self.showMaximized()
        # self.move(QApplication.desktop().screen().rect().center() - self.rect().center())
        self.setWindowTitle("NIDS")
        self.setWidgets()
        self.ui.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.ui.browseBut.connect(self.ui.browseBut, SIGNAL("clicked()"), lambda: self.browse())
        self.ui.saveBut.connect(self.ui.saveBut, SIGNAL("clicked()"), lambda : self.save())



    def setWidgets(self):
        mainFrame = QWidget()
        # Creating figure and canvas for standard
        self._fig = figure(facecolor=(0, 0, 0, 0.3))
        self._canvas = FigureCanvas(self._fig)
        self._canvas.setParent(mainFrame)
        self._canvas.setFocusPolicy(Qt.StrongFocus)


        #Creating figure and canvas for result
        self.fig = figure(facecolor=(0, 0, 0, 0.3))
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(mainFrame)
        self.canvas.setFocusPolicy(Qt.StrongFocus)



        #
        self.fig3 = figure(facecolor=(0, 0, 0, 0.3))
        self.canvas3 = FigureCanvas(self.fig3)
        self.canvas3.setParent(mainFrame)
        self.canvas3.setFocusPolicy(Qt.StrongFocus)


        #Adding Pie-Chart to form
        self.ui.std_piechart.addWidget(self._canvas)
        self.ui.res_piechart.addWidget(self.canvas)
        self.ui.bar.addWidget(self.canvas3)


        #3d scatter


        #Plotting the graph
        self.plot()



    def plot(self, ):
        label_set = 'Normal', 'Neptune', 'Smurf', 'Back', 'Teardrop', 'POD', 'Land', 'Anomalies'
        std_set=open('./file/std.txt', 'r')
        normal = float(std_set.readline())
        neptune = float(std_set.readline())
        smurf = float(std_set.readline())
        back = float(std_set.readline())
        teardrop = float(std_set.readline())
        pod = float(std_set.readline())
        land = float(std_set.readline())
        anomaly=float(std_set.readline())
        std_set.close()

        std_pie_data=[normal, neptune, smurf, back, teardrop, pod, land, anomaly]
        colors_std = [(0.47, 0.34, 0.64,1), (0.59, 0.74, 0.27,1), (0.24, 0.47, 0.76,1), 'yellowgreen',  'gray', 'blue', 'red', 'white']
        std_perct = std_pie_data / sum(std_pie_data) * 100
        std_labels=['%s	: %1.2f %%' % (l, s) for l, s in zip(label_set, std_perct)]
        plt.figure(1)
        patches, texts = plt.pie(std_pie_data, colors=colors_std, shadow=True, startangle=90)
        self.ui.stdSummary.setText('\n'.join(std_labels))

        plt.legend(labels=label_set, loc='best')
        plt.axis('equal')
        plt.tight_layout()


        file_temp=open('./file/temp.txt','w')
        file_temp.write('\nStatistics for Standard Value: \n')
        file_temp.write('\n'.join(std_labels))



# Plotting the result dataa
        F = open('./file/result.txt', 'r')
        normal = float(F.readline())
        neptune = float(F.readline())
        smurf = float(F.readline())
        back = float(F.readline())
        teardrop = float(F.readline())
        pod = float(F.readline())
        land = float(F.readline())
        anomaly = float(F.readline())
        F.close()

        res_pie_data = [normal, neptune, smurf, back, teardrop, pod, land, anomaly]

        if neptune==0 and smurf==0 and back==0 and teardrop==0 and pod==0 and land==0 and anomaly ==0:
           self.ui.res_summary.setText("There are no DOS or anomalies in given set.")
           self.ui.res_summary.setStyleSheet("background-color: rgba(1,1,1,0.5); color: rgb(0, 200, 0);")
        else:
            self.ui.res_summary.setText("There are some DOS attacks or anomalies in given set.")
            self.ui.res_summary.setStyleSheet("background-color: rgba(1,1,1,0.5); color: rgb(255, 0, 0);")
        self.ui.tot_val.setText(str(sum(res_pie_data)))
        self.ui.normal_res.setText(str(normal))
        self.ui.nep_res.setText(str(neptune))
        self.ui.smurf_res.setText(str(smurf))
        self.ui.back_res.setText(str(back))
        self.ui.tear_res.setText(str(teardrop))
        self.ui.pod_res.setText(str(pod))
        self.ui.land_res.setText(str(land))
        self.ui.anomaly_res.setText(str(anomaly))












        colors_res=['yellowgreen', (0.29, 0.48, 0.75,1), (1.00, 0.79, 0.00,1), 'lightskyblue', 'gray', 'blue', 'green', 'brown']
        res_perct = res_pie_data / sum(res_pie_data) * 100
        res_labels = ['%s	: %1.2f %%' % (l, s) for l, s in zip(label_set, res_perct)]
        plt.figure(2)
        patches, texts = plt.pie(res_pie_data, colors=colors_res, shadow=True, startangle=90)
        self.ui.resSummary.setText('\n'.join(res_labels))


        plt.legend(labels=label_set, loc='best')
        plt.axis('equal')
        plt.tight_layout()
        file_temp.write('\n__________________________________________________________________')
        file_temp.write("\nThe statistics for result data: ")
        file_temp.write('\n'.join(std_labels))
        file_temp.close()

        F = open('rate', 'r')
        norTP = float(F.readline())
        norFN = float(F.readline())
        nepTP = float(F.readline())
        nepFN = float(F.readline())
        smuTP = float(F.readline())
        smuFN = float(F.readline())
        F.close()

        norTPR = norTP / (norTP + norFN)
        nepTPR = nepTP / (nepTP + nepFN)
        smuTPR = smuTP / (smuTP + smuFN)

        objects = ('Normal', 'Neptune', 'Smurfs')
        y_pos = np.arange(len(objects))
        performance = [norTPR, nepTPR, smuTPR]
        plt.figure(3)
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('True Positive Rates')
        plt.title('Prediction result')






        #3d scatter graph





    def browse(self):

        self.ui.browser.setText(QFileDialog.getSaveFileName())


    def save(self):
        name=self.ui.browser.text()

        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")


        if name=='':

            msg.setText("Please choose the directory.")
            msg.show()
        else:
            try:
                temp_read=open('./file/temp.txt','r')
                file = open(name, 'w')
            except:
                msg.setText("Error has occured. Can't write to disk.")
                msg.show()
                return


            data = temp_read.read()
            temp_read.close()
            try:
                file.writelines(data)
                msg.setIcon(QMessageBox.Information)
                msg.setWindowTitle("Saved")
                msg.setText("Report has been saved.")
                msg.show()
                file.close()
            except:
                msg.setText("Error has occured. Can't write to disk.")
                msg.show()
                return



























