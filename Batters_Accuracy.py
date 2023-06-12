from PyQt5 import QtCore, QtGui, QtWidgets
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, f1_score, accuracy_score
import pandas as pd
import sys
from Barchart import Barchart
from sklearn import svm
from DBConnection import DBConnection
class Ui_BattersAccuracy(object):


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
                "select Innings,BA,SR,Centuries,Fifties,Zeros,HS,Rating from batters")
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
                x_train.append(float(r[6]))
                y_train.append(int(r[7]))
                trainset.append(x_train)
            trainset = np.array(trainset)
            #print("trd=", trainset)

            # Train the model
            y_train = np.array(y_train)

            tf = pd.read_csv(file)
            testdata = np.array(tf.drop(['Rating'], 1))
            #print("td=", testdata)
            testdata = testdata.reshape(len(testdata), -1)
            y_test=tf["Rating"]

            print("y_test",y_test)

            print("NaiveBayesClassifier")
            nb = MultinomialNB()
            nb.fit(trainset, y_train)
            pridctcls = nb.predict(testdata)
            nb_acurcy =accuracy_score(y_test, pridctcls)* 100

            print("DecisionTreeClassifier")
            dt = DecisionTreeClassifier()
            dt.fit(trainset, y_train)
            pridctcls = dt.predict(testdata)
            dt_acurcy=accuracy_score(y_test, pridctcls)* 100

            print("RandomForestClassifier")
            rf = RandomForestClassifier()
            rf.fit(trainset, y_train)
            pridctcls = rf.predict(testdata)  # Predicting
            rf_acurcy=accuracy_score(y_test, pridctcls)*100
            #print("Result=", result)
            #print(round(accuracy_score(y_test, result),3)*100)
            #return result
            print("SVMClassifier")
            clf =  svm.SVC()
            clf.fit(trainset, y_train)
            pridctcls = clf.predict(testdata)  # Predicting
            svm_acurcy = accuracy_score(y_test, pridctcls) * 100
            self.showMessageBox("Information", "Classification Completed..!")
            list = []
            list.clear()
            list.append(nb_acurcy)
            list.append(dt_acurcy)
            list.append(rf_acurcy)
            list.append(svm_acurcy)
            b = Barchart()
            b.view(list)






        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

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
        Dialog.setWindowTitle(_translate("Dialog", "Batters Accuracy"))
        self.label.setText(_translate("Dialog", "Classify  Batters Accuracy"))
        self.label_2.setText(_translate("Dialog", "Select Testing File"))
        self.pushButton.setText(_translate("Dialog", "Accuracy"))
        self.pushButton_2.setText(_translate("Dialog", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_BattersPerformance()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

