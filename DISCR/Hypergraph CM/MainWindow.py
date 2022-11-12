# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(489, 9, 201, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.btnSetupGraph = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnSetupGraph.setObjectName("btnSetupGraph")
        self.verticalLayout.addWidget(self.btnSetupGraph)
        self.btnColorGraph = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnColorGraph.setObjectName("btnColorGraph")
        self.verticalLayout.addWidget(self.btnColorGraph)
        self.btnShowGraph = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnShowGraph.setObjectName("btnShowGraph")
        self.verticalLayout.addWidget(self.btnShowGraph)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.spboxVertex = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spboxVertex.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spboxVertex.setMinimum(1)
        self.spboxVertex.setMaximum(100000000)
        self.spboxVertex.setObjectName("spboxVertex")
        self.verticalLayout.addWidget(self.spboxVertex)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.spboxEdges = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spboxEdges.setMaximumSize(QtCore.QSize(100, 16777215))
        self.spboxEdges.setMaximum(100000000)
        self.spboxEdges.setObjectName("spboxEdges")
        self.verticalLayout.addWidget(self.spboxEdges)
        self.lblColors = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lblColors.setObjectName("lblColors")
        self.verticalLayout.addWidget(self.lblColors)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btnExit = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btnExit.setObjectName("btnExit")
        self.verticalLayout.addWidget(self.btnExit)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(9, 9, 471, 451))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget_2)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 467, 447))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tblMatrix = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.tblMatrix.setGeometry(QtCore.QRect(-5, 1, 471, 451))
        self.tblMatrix.setObjectName("tblMatrix")
        self.tblMatrix.setColumnCount(0)
        self.tblMatrix.setRowCount(0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Раскраска вершин гиперграфа"))
        self.btnSetupGraph.setText(_translate("MainWindow", "Задать граф"))
        self.btnColorGraph.setText(_translate("MainWindow", "Раскрасить граф"))
        self.btnShowGraph.setText(_translate("MainWindow", "Посмотреть граф"))
        self.label.setText(_translate("MainWindow", " Количество вершин"))
        self.label_2.setText(_translate("MainWindow", "Количество рёбер"))
        self.lblColors.setText(_translate("MainWindow", "Цветов получилось:"))
        self.btnExit.setText(_translate("MainWindow", "Выход"))