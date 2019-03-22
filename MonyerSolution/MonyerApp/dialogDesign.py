# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialogDesign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(228, 213)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.titleLabel = QtWidgets.QLabel(Dialog)
        self.titleLabel.setObjectName("titleLabel")
        self.horizontalLayout.addWidget(self.titleLabel)
        self.titleEdit = QtWidgets.QLineEdit(Dialog)
        self.titleEdit.setMaxLength(255)
        self.titleEdit.setObjectName("titleEdit")
        self.horizontalLayout.addWidget(self.titleEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.amounLabel = QtWidgets.QLabel(Dialog)
        self.amounLabel.setObjectName("amounLabel")
        self.horizontalLayout_2.addWidget(self.amounLabel)
        self.amountEdit = QtWidgets.QDoubleSpinBox(Dialog)
        self.amountEdit.setMinimum(0.0)
        self.amountEdit.setMaximum(10000.0)
        self.amountEdit.setObjectName("amountEdit")
        self.horizontalLayout_2.addWidget(self.amountEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.typeLabel = QtWidgets.QLabel(Dialog)
        self.typeLabel.setObjectName("typeLabel")
        self.horizontalLayout_3.addWidget(self.typeLabel)
        self.expenseRadioButton = QtWidgets.QRadioButton(Dialog)
        self.expenseRadioButton.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expenseRadioButton.sizePolicy().hasHeightForWidth())
        self.expenseRadioButton.setSizePolicy(sizePolicy)
        self.expenseRadioButton.setMouseTracking(True)
        self.expenseRadioButton.setTabletTracking(False)
        self.expenseRadioButton.setAcceptDrops(False)
        self.expenseRadioButton.setChecked(True)
        self.expenseRadioButton.setObjectName("expenseRadioButton")
        self.horizontalLayout_3.addWidget(self.expenseRadioButton)
        self.IncomeRadioButton = QtWidgets.QRadioButton(Dialog)
        self.IncomeRadioButton.setObjectName("IncomeRadioButton")
        self.horizontalLayout_3.addWidget(self.IncomeRadioButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.dateLabel = QtWidgets.QLabel(Dialog)
        self.dateLabel.setObjectName("dateLabel")
        self.horizontalLayout_4.addWidget(self.dateLabel)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(Dialog)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.horizontalLayout_4.addWidget(self.dateTimeEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.titleLabel.setBuddy(self.titleEdit)
        self.typeLabel.setBuddy(self.expenseRadioButton)
        self.dateLabel.setBuddy(self.dateTimeEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.titleLabel.setText(_translate("Dialog", "Title:"))
        self.amounLabel.setText(_translate("Dialog", "Amount:"))
        self.typeLabel.setText(_translate("Dialog", "Type:"))
        self.expenseRadioButton.setText(_translate("Dialog", "Expense"))
        self.IncomeRadioButton.setText(_translate("Dialog", "Income"))
        self.dateLabel.setText(_translate("Dialog", "Date and Time:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

