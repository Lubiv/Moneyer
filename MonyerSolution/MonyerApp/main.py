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

    def refresh(self):
        incomeCount = 0
        expenceCount = 0
        for index, row in self.current_balance.balance.iterrows():
            if index == 0:
                self.initialLabel.setText(str(row["amount"]))
            else:
                titleLabel = QtWidgets.QLabel(row["title"])
                titleLabel.setObjectName("titleLabel%d" % index)
                amountLabel = QtWidgets.QLabel(str(row["amount"]))
                amountLabel.setObjectName("amountLabel%d" % index)
                dateTimeLabel = QtWidgets.QLabel(row["dateTime"])
                dateTimeLabel.setObjectName("dateTimeLabel%d" % index)

                layout = QtWidgets.QHBoxLayout();
                layout.setObjectName("transaction%d" % index)
                layout.addWidget(titleLabel, 0)
                layout.addWidget(amountLabel, 1)
                layout.addWidget(dateTimeLabel, 2)

                col = 0 
                if row["isExpense"]:
                    col = 1
                    expenceCount =+ 1
                else:
                    incomeCount =+ 1


                self.gridLayout.addLayout(layout,1 + incomeCount if col == 0 else 1 + expenceCount, col)                


class Dialog(QtWidgets.QDialog, dialogDesign.Ui_Dialog):
    def __init__(self, current_balance, parent=None):
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        self.current_balance = current_balance
        self.buttonBox.accepted.connect(self.take_data)
        self.buttonBox.accepted.connect(parent.refresh)
        self.buttonBox.rejected.connect(self.close)
        self.buttonBox.rejected.connect(parent.refresh)

        

    def take_data(self):
        transaction = Transaction(self.titleEdit.text(),
                                  self.amountEdit.value(),
                                  self.expenseRadioButton.isChecked(),
                                  self.dateTimeEdit.dateTime().toString(self.dateTimeEdit.displayFormat()))
        self.current_balance.add(transaction)
        self.current_balance.save()
        self.close()
        

def main():
    current_balance = Balance(10)
    current_balance.load('test.csv')
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = Program(current_balance)
    mainWindow.show()
    mainWindow.refresh()
    app.exec_()

if __name__ == '__main__':
    main()
