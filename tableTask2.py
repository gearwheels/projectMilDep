# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tableTask2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_tableTask2Widget(object):
    def setupUi(self, tableTask2Widget):
        tableTask2Widget.setObjectName("tableTask2Widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(tableTask2Widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(tableTask2Widget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setMinimumWidth(145)
        self.tableWidget.setMaximumWidth(145)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setHorizontalHeaderLabels(["Ранний срок"]) #, "Поздний срок"
        
        self.verticalLayout.addWidget(self.tableWidget)
        self.tableCheckButton = QtWidgets.QPushButton(tableTask2Widget)
        self.tableCheckButton.setObjectName("tableCheckButton")
        self.tableCheckButton.setFont(font)
        self.verticalLayout.addWidget(self.tableCheckButton)

        self.retranslateUi(tableTask2Widget)
        QtCore.QMetaObject.connectSlotsByName(tableTask2Widget)

    def retranslateUi(self, tableTask2Widget):
        _translate = QtCore.QCoreApplication.translate
        tableTask2Widget.setWindowTitle(_translate("tableTask2Widget", "Form"))
        self.tableCheckButton.setText(_translate("tableTask2Widget", "Заполнить"))

