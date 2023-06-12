
from PyQt5 import QtCore, QtGui, QtWidgets
from Coach import Ui_Coach
from Captain import Ui_Captain
class Ui_Dialog(object):

    def coachlogin(self, event):
        try:
            self.admn = QtWidgets.QDialog()
            self.ui = Ui_Coach(self.admn)
            self.ui.setupUi(self.admn)
            self.admn.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def captainlogin(self, event):
        try:
            self.cap = QtWidgets.QDialog()
            self.ui = Ui_Captain(self.cap)
            self.ui.setupUi(self.cap)
            self.cap.show()
        except Exception as e:
            print(e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)
        event.accept()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(741, 517)
        Dialog.setStyleSheet("background-color: rgb(170, 170, 0);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(80, 30, 631, 81))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"Franklin Gothic Heavy\";")
        self.label.setObjectName("label")
        self.captain = QtWidgets.QLabel(Dialog)
        self.captain.setGeometry(QtCore.QRect(390, 210, 241, 161))
        self.captain.setStyleSheet("image: url(../Cricket/images/user.png);")
        self.captain.setText("")
        self.captain.setObjectName("captain")
        self.captain.mousePressEvent = self.captainlogin
        self.coach = QtWidgets.QLabel(Dialog)
        self.coach.setGeometry(QtCore.QRect(50, 210, 271, 151))
        self.coach.setStyleSheet("image: url(../Cricket/images/coach.png);")
        self.coach.setText("")
        self.coach.setObjectName("coach")
        self.coach.mousePressEvent = self.coachlogin
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(160, 380, 121, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(480, 380, 121, 31))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 80, 381, 61))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 14pt \"Franklin Gothic Heavy\";")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Main"))
        self.label.setText(_translate("Dialog", "PREDICTION ACCURACY IN THE GAME OF CRICKET"))
        self.label_2.setText(_translate("Dialog", "Coach"))
        self.label_3.setText(_translate("Dialog", "Captain"))
        self.label_4.setText(_translate("Dialog", "USING MACHINE LEARNING"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

