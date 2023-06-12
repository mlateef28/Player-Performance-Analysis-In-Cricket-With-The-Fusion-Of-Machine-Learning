
from PyQt5 import QtCore, QtGui, QtWidgets
from DBConnection import DBConnection
import xlrd
import sys
class Ui_BowllersDataset(object):

    def __init__(self,Dialog):
        self.dialog=Dialog

    def trainingset(self):
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File")
        self.lineEdit.setText(fileName)

    def upload(self):
        try:
            fname = self.lineEdit.text()
            book = xlrd.open_workbook(fname)
            sheet = book.sheet_by_index(0)
            database = DBConnection.getConnection()
            cursor = database.cursor()
            cursor.execute("delete from bowlers")
            database.commit()
            query = "insert into bowlers values(%s,%s,%s,%s,%s,%s,%s)"
            for r in range(1, sheet.nrows):
                innings = sheet.cell(r, 0).value
                bals= sheet.cell(r, 1).value
                balavg = sheet.cell(r, 2).value
                sr = sheet.cell(r, 3).value
                fours = sheet.cell(r, 4).value
                fives = sheet.cell(r, 5).value
                rating = sheet.cell(r, 6).value
                values = (str(innings), str(bals), str(balavg), str(sr), str(fours), str(fives), int(rating))
                cursor.execute(query, values)
                database.commit()
                print("inserted")

            self.showMessageBox("Information", "Uploaded Successfully..!")
            self.dialog.hide()
        except Exception as e:
            print(e.args[0])
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
        Dialog.resize(652, 471)
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
        self.pushButton.setGeometry(QtCore.QRect(170, 280, 181, 41))
        self.pushButton.setStyleSheet("background-color: rgb(170, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Verdana\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.upload)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(480, 202, 91, 31))
        self.pushButton_2.setStyleSheet("\n"
"color: rgb(255, 255, 255);\n"
"font: 12pt \"Franklin Gothic Heavy\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.trainingset)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bowllers Dataset"))
        self.label.setText(_translate("Dialog", "Upload Bowllers Dataset"))
        self.label_2.setText(_translate("Dialog", "Select File"))
        self.pushButton.setText(_translate("Dialog", "Upload"))
        self.pushButton_2.setText(_translate("Dialog", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_BowllersDataset()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

