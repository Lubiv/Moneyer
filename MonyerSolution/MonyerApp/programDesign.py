# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'programDesign.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(539, 260)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setMaximumSize(QtCore.QSize(16777215, 19))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.IncomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.IncomeLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.IncomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IncomeLabel.setObjectName("IncomeLabel")
        self.gridLayout.addWidget(self.IncomeLabel, 1, 0, 1, 1)
        self.initialLabel = QtWidgets.QLabel(self.centralwidget)
        self.initialLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.initialLabel.setText("")
        self.initialLabel.setObjectName("initialLabel")
        self.gridLayout.addWidget(self.initialLabel, 0, 1, 1, 1)
        self.expenseLable = QtWidgets.QLabel(self.centralwidget)
        self.expenseLable.setMaximumSize(QtCore.QSize(16777215, 20))
        self.expenseLable.setAlignment(QtCore.Qt.AlignCenter)
        self.expenseLable.setObjectName("expenseLable")
        self.gridLayout.addWidget(self.expenseLable, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 539, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.titleLabel.setText(_translate("MainWindow", "Balance"))
        self.label_4.setText(_translate("MainWindow", "Initial balance:"))
        self.IncomeLabel.setText(_translate("MainWindow", "Income"))
        self.expenseLable.setText(_translate("MainWindow", "Expense"))
        self.addButton.setText(_translate("MainWindow", "Add Transaction"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

