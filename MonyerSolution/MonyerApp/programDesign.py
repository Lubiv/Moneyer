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
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.expenseLable = QtWidgets.QLabel(self.centralwidget)
        self.expenseLable.setMaximumSize(QtCore.QSize(16777215, 20))
        self.expenseLable.setAlignment(QtCore.Qt.AlignCenter)
        self.expenseLable.setObjectName("expenseLable")
        self.gridLayout.addWidget(self.expenseLable, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_2.addWidget(self.label_8)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_2.addWidget(self.label_10)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.IncomeLabel = QtWidgets.QLabel(self.centralwidget)
        self.IncomeLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.IncomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.IncomeLabel.setObjectName("IncomeLabel")
        self.gridLayout.addWidget(self.IncomeLabel, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)
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
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.label_2.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
        self.expenseLable.setText(_translate("MainWindow", "Expense"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.IncomeLabel.setText(_translate("MainWindow", "Income"))
        self.label_6.setText(_translate("MainWindow", "Current balance:"))
        self.label_4.setText(_translate("MainWindow", "Initial balance:"))
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

