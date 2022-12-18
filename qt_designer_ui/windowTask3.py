# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowTask3.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow3(object):
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(1603, 1253)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow3.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setIconSize(QtCore.QSize(47, 42))
        self.toolBar.setObjectName("toolBar")
        MainWindow3.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow3)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1603, 21))
        self.menuBar.setStyleSheet("background-color: #b8ffc0;")
        self.menuBar.setObjectName("menuBar")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuTask3 = QtWidgets.QMenu(self.menuBar)
        self.menuTask3.setObjectName("menuTask3")
        MainWindow3.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow3)
        self.statusbar.setStyleSheet("background-color: #b8ffc0;")
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)
        self.actionNewFile = QtWidgets.QAction(MainWindow3)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/iconePack/file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNewFile.setIcon(icon)
        self.actionNewFile.setObjectName("actionNewFile")
        self.actionOpenFile = QtWidgets.QAction(MainWindow3)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("resources/iconePack/write.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpenFile.setIcon(icon1)
        self.actionOpenFile.setObjectName("actionOpenFile")
        self.actionSaveFile = QtWidgets.QAction(MainWindow3)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("resources/iconePack/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveFile.setIcon(icon2)
        self.actionSaveFile.setObjectName("actionSaveFile")
        self.actionSaveFileAs = QtWidgets.QAction(MainWindow3)
        self.actionSaveFileAs.setObjectName("actionSaveFileAs")
        self.actionForward = QtWidgets.QAction(MainWindow3)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("resources/iconePack/forward.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionForward.setIcon(icon3)
        self.actionForward.setObjectName("actionForward")
        self.actionBackward = QtWidgets.QAction(MainWindow3)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("resources/iconePack/reply.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionBackward.setIcon(icon4)
        self.actionBackward.setObjectName("actionBackward")
        self.actionbtnMoveNode = QtWidgets.QAction(MainWindow3)
        self.actionbtnMoveNode.setCheckable(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("resources/iconePack/axis_arrow_icon_138909.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnMoveNode.setIcon(icon5)
        font = QtGui.QFont()
        self.actionbtnMoveNode.setFont(font)
        self.actionbtnMoveNode.setPriority(QtWidgets.QAction.NormalPriority)
        self.actionbtnMoveNode.setObjectName("actionbtnMoveNode")
        self.actionbtnInfo = QtWidgets.QAction(MainWindow3)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("resources/iconePack/attachment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnInfo.setIcon(icon6)
        self.actionbtnInfo.setObjectName("actionbtnInfo")
        self.actionbtnHome = QtWidgets.QAction(MainWindow3)
        self.actionbtnHome.setCheckable(True)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("resources/iconePack/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnHome.setIcon(icon7)
        self.actionbtnHome.setObjectName("actionbtnHome")
        self.actionbtnZoomIn = QtWidgets.QAction(MainWindow3)
        self.actionbtnZoomIn.setCheckable(False)
        self.actionbtnZoomIn.setChecked(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("resources/iconePack/zoom-in.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnZoomIn.setIcon(icon8)
        self.actionbtnZoomIn.setAutoRepeat(True)
        self.actionbtnZoomIn.setObjectName("actionbtnZoomIn")
        self.actionbtnZoomOut = QtWidgets.QAction(MainWindow3)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("resources/iconePack/zoom-out.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnZoomOut.setIcon(icon9)
        self.actionbtnZoomOut.setObjectName("actionbtnZoomOut")
        self.actionHelpTask = QtWidgets.QAction(MainWindow3)
        self.actionHelpTask.setObjectName("actionHelpTask")
        self.actionHelpProgram = QtWidgets.QAction(MainWindow3)
        self.actionHelpProgram.setObjectName("actionHelpProgram")
        self.actionSetting = QtWidgets.QAction(MainWindow3)
        self.actionSetting.setObjectName("actionSetting")
        self.actionbtnCheck = QtWidgets.QAction(MainWindow3)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("resources/iconePack/check-mark.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnCheck.setIcon(icon10)
        self.actionbtnCheck.setObjectName("actionbtnCheck")
        self.actionbtnDottedConnectNode = QtWidgets.QAction(MainWindow3)
        self.actionbtnDottedConnectNode.setCheckable(True)
        self.actionbtnDottedConnectNode.setEnabled(True)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("resources/iconePack/arrowsDotted.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionbtnDottedConnectNode.setIcon(icon11)
        self.actionbtnDottedConnectNode.setObjectName("actionbtnDottedConnectNode")
        self.actionHelp = QtWidgets.QAction(MainWindow3)
        self.actionHelp.setCheckable(True)
        self.actionHelp.setEnabled(False)
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("resources/iconePack/help.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon12)
        self.actionHelp.setObjectName("actionHelp")
        self.actionHelpStud = QtWidgets.QAction(MainWindow3)
        self.actionHelpStud.setObjectName("actionHelpStud")
        self.actionHelpTeach = QtWidgets.QAction(MainWindow3)
        self.actionHelpTeach.setObjectName("actionHelpTeach")
        self.actionViewTask = QtWidgets.QAction(MainWindow3)
        self.actionViewTask.setObjectName("actionViewTask")
        self.actionSolveTask = QtWidgets.QAction(MainWindow3)
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("resources/iconePack/document.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSolveTask.setIcon(icon13)
        self.actionSolveTask.setObjectName("actionSolveTask")
        self.toolBar.addAction(self.actionbtnMoveNode)
        self.toolBar.addAction(self.actionbtnDottedConnectNode)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionbtnCheck)
        self.toolBar.addAction(self.actionbtnInfo)
        self.toolBar.addAction(self.actionHelp)
        # self.toolBar.addAction(self.actionSolveTask)
        self.toolBar.addAction(self.actionbtnHome)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionHelpStud)
        self.menuHelp.addAction(self.actionHelpTeach)
        self.menuTask3.addAction(self.actionViewTask)
        self.menuBar.addAction(self.menuHelp.menuAction())
        self.menuBar.addAction(self.menuTask3.menuAction())

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "Задание 3"))
        self.toolBar.setWindowTitle(_translate("MainWindow3", "toolBar"))
        self.menuHelp.setTitle(_translate("MainWindow3", "Справка"))
        self.menuTask3.setTitle(_translate("MainWindow3", "Задание 3"))
        self.actionNewFile.setText(_translate("MainWindow3", "Новый файл"))
        self.actionNewFile.setToolTip(_translate("MainWindow3", "Создать новый файл"))
        self.actionOpenFile.setText(_translate("MainWindow3", "Открыть файл"))
        self.actionSaveFile.setText(_translate("MainWindow3", "Сохранить"))
        self.actionSaveFileAs.setText(_translate("MainWindow3", "Сохранить как"))
        self.actionForward.setText(_translate("MainWindow3", "Вперед        Ctrl+Y"))
        self.actionBackward.setText(_translate("MainWindow3", "Назад          Ctrl+Z"))
        self.actionbtnMoveNode.setText(_translate("MainWindow3", "btnMoveNode"))
        self.actionbtnMoveNode.setToolTip(_translate("MainWindow3", "Передвинуть элемент"))
        self.actionbtnInfo.setText(_translate("MainWindow3", "btnInfo"))
        self.actionbtnInfo.setToolTip(_translate("MainWindow3", "Материалы"))
        self.actionbtnHome.setText(_translate("MainWindow3", "btnHome"))
        self.actionbtnHome.setToolTip(_translate("MainWindow3", "Перейти к выбору заданий / В меню"))
        self.actionbtnZoomIn.setText(_translate("MainWindow3", "btnZoomIn"))
        self.actionbtnZoomIn.setToolTip(_translate("MainWindow3", "Увеличить изображение"))
        self.actionbtnZoomOut.setText(_translate("MainWindow3", "btnZoomOut"))
        self.actionbtnZoomOut.setToolTip(_translate("MainWindow3", "Уменьшить изображение"))
        self.actionHelpTask.setText(_translate("MainWindow3", "Справка по заданию"))
        self.actionHelpProgram.setText(_translate("MainWindow3", "Справка по программе "))
        self.actionSetting.setText(_translate("MainWindow3", "Настройки программы"))
        self.actionbtnCheck.setText(_translate("MainWindow3", "btnCheck"))
        self.actionbtnCheck.setToolTip(_translate("MainWindow3", "<html><head/><body><p>Проверить задание</p></body></html>"))
        self.actionbtnDottedConnectNode.setText(_translate("MainWindow3", "btnDottedConnectNode"))
        self.actionbtnDottedConnectNode.setToolTip(_translate("MainWindow3", "Перемещение пунктирной стрелки"))
        self.actionHelp.setText(_translate("MainWindow3", "подсказка"))
        self.actionHelp.setToolTip(_translate("MainWindow3", "подсказка (режим преподавателя)"))
        self.actionHelpStud.setText(_translate("MainWindow3", "студенту"))
        self.actionHelpTeach.setText(_translate("MainWindow3", "преподавателю"))
        self.actionViewTask.setText(_translate("MainWindow3", "Задание 3"))
        self.actionSolveTask.setText(_translate("MainWindow3", "SolveTask"))
        self.actionSolveTask.setToolTip(_translate("MainWindow3", "решить задание (режим преподавателя)"))