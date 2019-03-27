from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from datetime import date
from datetime import timedelta
import sys
import os

import programDesign, dialogDesign, beginningDesign
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

    def deleteItemsOfLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.setParent(None)
                else:
                    self.deleteItemsOfLayout(item.layout())

    def refresh(self):
        incomeCount = 0
        expenseCount = 0
        initial = 0.0
        totalIncome = 0.0
        totalExpense = 0.0
        final = 0.0
        self.deleteItemsOfLayout(self.gridLayout)
        for index, row in self.current_balance.balance.iterrows():
            if index == 0:
                initial = row["amount"]
                self.gridLayout.addWidget(QtWidgets.QLabel('Initial balance: %.2f' % initial),0,0)
                self.gridLayout.addWidget(QtWidgets.QLabel('Income'),1,0)
                self.gridLayout.addWidget(QtWidgets.QLabel('Expense'),1,1)
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
                    expenseCount += 1
                    totalExpense += row['amount']
                else:
                    incomeCount += 1
                    totalIncome += row['amount']

                self.gridLayout.addLayout(layout,1 + incomeCount if col == 0 else 1 + expenseCount, col)
                
        final = initial + totalIncome - totalExpense

        self.gridLayout.addWidget(QtWidgets.QLabel('Total income: %.2f' % totalIncome), 2 + max(incomeCount, expenseCount), 0)
        self.gridLayout.addWidget(QtWidgets.QLabel('Total expense: %.2f' % totalExpense), 2 + max(incomeCount, expenseCount), 1)
        self.gridLayout.addWidget(QtWidgets.QLabel('Current Balance: %.2f' % final), 3 + max(incomeCount, expenseCount), 0)

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
        self.accept()

class Beginning(QtWidgets.QDialog, beginningDesign.Ui_Dialog):
    def __init__(self, parent=None):
        super(Beginning, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.close)

        

    def return_initial(self):
        return self.doubleSpinBox.value()

    @staticmethod
    def get_initial(parent=None):
        dialog = Beginning(parent)
        dialog.exec_()
        return dialog.return_initial()
        

def subtract_one_month(dt0):
    dt1 = dt0.replace(day=1)
    dt2 = dt1 - timedelta(days=1)
    dt3 = dt2.replace(day=1)
    return dt3

def get_past_final(path):
    past_balance = Balance(path)
    initial = 0.0
    totalIncome = 0.0
    totalExpense = 0.0

    for index, row in past_balance.balance.iterrows():
        if index == 0:
            initial = row["amount"]
        else:
            if row["isExpense"]:
                totalExpense += row['amount']
            else:
                totalIncome += row['amount']
                
    return initial + totalIncome - totalExpense

def main():
    app = QtWidgets.QApplication(sys.argv)
    
    current_path = '%s.csv' % date.today().strftime("%m-%y")
    past_path = '%s.csv' % subtract_one_month(date.today()).strftime("%m-%y")
    current_exists = os.path.isfile(current_path)
    past_exists = os.path.isfile(past_path)
    if current_exists:
        current_balance = Balance(current_path)
    elif past_exists:
        current_balance = Balance(get_past_final(past_path))
        current_balance.save()
    else:
        dialog = Beginning()
        current_balance = Balance(dialog.get_initial())
        current_balance.save()

    mainWindow = Program(current_balance)
    mainWindow.show()
    mainWindow.refresh()
    app.exec_()

if __name__ == '__main__':
    main()
