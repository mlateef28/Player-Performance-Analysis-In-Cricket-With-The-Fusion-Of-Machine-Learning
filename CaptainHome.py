from PyQt5 import QtCore, QtGui, QtWidgets
from Batters_dataset import Ui_BattersDataset
from Bowllers_dataset import Ui_BowllersDataset
from ViewBatters import Ui_ViewBatters
from ViewBowllers import Ui_ViewBowllers
from Batters_Performance import Ui_BattersPerformance
from Bowlers_Performance import Ui_BowlersPerformance
from Batters_Accuracy import Ui_BattersAccuracy
from Bowllers_Accuracy import Ui_BowllersAccuracy
class Ui_CaptainHome(object):

    def batters_performance(self):
        try:
            self.battrs = QtWidgets.QDialog()
            self.ui = Ui_BattersPerformance()
            self.ui.setupUi(self.battrs)
            self.battrs.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def bowllers(self):
        try:
            self.bwlrs = QtWidgets.QDialog()
            self.ui = Ui_BowlersPerformance()
            self.ui.setupUi(self.bwlrs)
            self.bwlrs.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def battersacuracy(self):
        try:
            self.btrs = QtWidgets.QDialog()
            self.ui = Ui_BattersAccuracy()
            self.ui.setupUi(self.btrs)
            #self.ui.view()
            self.btrs.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def bowlerslist(self):
        try:
            self.blrs = QtWidgets.QDialog()
            self.ui = Ui_ViewBowllers()
            self.ui.setupUi(self.blrs)
            self.ui.view()
            self.blrs.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def bowlersacury(self):
        try:
            self.btrs = QtWidgets.QDialog()
            self.ui = Ui_BowllersAccuracy()
            self.ui.setupUi(self.btrs)
            # self.ui.view()
            self.btrs.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)



    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(730, 494)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 70, 251, 51))
        self.pushButton.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 127);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.batters_performance)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 160, 251, 51))
        self.pushButton_2.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.bowllers)

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 250, 251, 51))
        self.pushButton_3.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 127);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.battersacuracy)
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(240, 340, 251, 51))
        self.pushButton_4.setStyleSheet("font: 12pt \"Franklin Gothic Heavy\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 85, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.bowlersacury)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Captain Home"))
        self.pushButton.setText(_translate("Dialog", "Batters Performance"))
        self.pushButton_2.setText(_translate("Dialog", "Bowlers Performance"))
        self.pushButton_3.setText(_translate("Dialog", "Batters Accuray"))
        self.pushButton_4.setText(_translate("Dialog", "Bowlers Accuracy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_CaptainHome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

