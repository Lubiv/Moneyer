from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import sys

import programDesign, dialogDesign
from Transaction import *
from Balance import *

class Program(QtWidgets.QMainWindow, programDesign.Ui_MainWindow):
    def __init__(self, current_balance, parent=None):
        super(Program, self).__init__(parent)
        self.setupUi(self)
        self.current_balance = current_balance
        self.addButton.clicked.connect(self.add_transaction)

    def add_transaction(self):
        dialog = Dialog(self.current_balance, self)
        dialog.show()

class Dialog(QtWidgets.QDialog, dialogDesign.Ui_Dialog):
    def __init__(self, current_balance, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.current_balance = current_balance
        self.buttonBox.accepted.connect(self.take_data)
        self.buttonBox.rejected.connect(self.close)

        

    def take_data(self):
        transaction = Transaction(self.titleEdit.text(),
                                  self.amountEdit.value(),
                                  self.expenseRadioButton.isChecked(),
                                  self.dateTimeEdit.dateTime().toString(self.dateTimeEdit.displayFormat()))
        self.current_balance.add(transaction)
        self.close()
        

def main():
    current_balance = Balance(10)
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Program(current_balance)
    mainWindow.show()
    app.exec_()

if __name__ == '__main__':
    main()

