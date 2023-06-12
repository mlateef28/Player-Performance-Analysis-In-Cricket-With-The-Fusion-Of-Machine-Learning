from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
import sys
from DBConnection import DBConnection
class Ui_BowlersPerformance(object):


    def testingset(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        self.lineEdit.setText(fileName)

    def predict(self):
        try:
            file=self.lineEdit.text()
            trainset = []
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute(
                "select Innings,Balls,Bowlavg,BSR,Fours,Fives,Rating from bowlers")
            row = cursor.fetchall()
            y_train = []
            trainset.clear()
            y_train.clear()
            for r in row:
                x_train = []
                x_train.clear()
                x_train.append(float(r[0]))
                x_train.append(float(r[1]))
                x_train.append(float(r[2]))
                x_train.append(float(r[3]))
                x_train.append(float(r[4]))
                x_train.append(float(r[5]))
                y_train.append(r[6])
                trainset.append(x_train)
           # print("y=", y_train)
           # print("trd=", trainset)
            trainset = np.array(trainset)
            #print("trd=", trainset)

            # Train the model
            y_train = np.array(y_train)

            tf = pd.read_csv(file)
            testdata = np.array(tf)
            #print("td=", testdata)
            testdata = testdata.reshape(len(testdata), -1)

            rf = RandomForestClassifier()
            rf.fit(trainset, y_train)
            result = rf.predict(testdata)  # Predicting
            print("Result=", result)
            # print(round(metrics.accuracy_score(y_train, result),3)*100)
            return result
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(652, 501)
        Dialog.setStyleSheet("background-color: rgb(0, 85, 127);")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(180, 80, 331, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 165, 141, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"Franklin Gothic Heavy\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(70, 200, 381, 41))
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 75 12pt \"Verdana\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 280, 181, 41))
        self.pushButton.setStyleSheet("background-color: rgb(170, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Verdana\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.predict)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 202, 91, 31))
        self.pushButton_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.testingset)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bowlers Performance"))
        self.label.setText(_translate("Dialog", "Predict  Bowlers Performance"))
        self.label_2.setText(_translate("Dialog", "Select Testing File"))
        self.pushButton.setText(_translate("Dialog", "Predict"))
        self.pushButton_2.setText(_translate("Dialog", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_BowlersPerformance()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

