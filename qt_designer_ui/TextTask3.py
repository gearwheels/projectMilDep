# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextTask3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextTask3(object):
    def setupUi(self, TextTask3):
        TextTask3.setObjectName("TextTask3")
        TextTask3.resize(795, 210)
        self.verticalLayout = QtWidgets.QVBoxLayout(TextTask3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(TextTask3)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(TextTask3)
        QtCore.QMetaObject.connectSlotsByName(TextTask3)

    def retranslateUi(self, TextTask3):
        _translate = QtCore.QCoreApplication.translate
        TextTask3.setWindowTitle(_translate("TextTask3", "Задание 3"))
        self.label.setText(_translate("TextTask3", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Задание 3</span><br/></p><p><span style=\" font-size:14pt;\">1. Расставьте вершины графа по верным временным осям в ранних сроках.</span></p><p><span style=\" font-size:14pt;\">2. Передвигая конец стрелки, поставьте стрелку на нужную ось, тем самым указывая продолжительность работ в ранних сроках. (Пунктирная линия - запас времени).</span></p><p><br/></p></body></html>"))
