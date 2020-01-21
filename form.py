# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Form.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 780)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 780))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 780))
        MainWindow.setStyleSheet("background-color: rgb(232, 246, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(850, 640, 211, 28))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.startButton.setFont(font)
        self.startButton.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.startButton.setObjectName("startButton")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 90, 141, 81))
        self.widget.setStyleSheet("border-image: url(:/images/arrow_right_next_forward_icon.png) 0 0 0 0 stretch stretch;")
        self.widget.setObjectName("widget")
        self.middleArrivalTime = QtWidgets.QLineEdit(self.widget)
        self.middleArrivalTime.setGeometry(QtCore.QRect(0, 27, 81, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.middleArrivalTime.setFont(font)
        self.middleArrivalTime.setWhatsThis("")
        self.middleArrivalTime.setStyleSheet("border-image: none;\n"
"background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.middleArrivalTime.setObjectName("middleArrivalTime")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(440, 60, 141, 141))
        self.widget_2.setStyleSheet("border-image: url(:/images/rocket_startup_monitor_screen_computer_icon.png);")
        self.widget_2.setObjectName("widget_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(730, 520, 451, 111))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(37, 56, 144);")
        self.groupBox.setObjectName("groupBox")
        self.radioButtonTask = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonTask.setGeometry(QtCore.QRect(20, 40, 171, 20))
        font = QtGui.QFont()
        font.setFamily("Niagara Solid")
        font.setPointSize(10)
        self.radioButtonTask.setFont(font)
        self.radioButtonTask.setChecked(True)
        self.radioButtonTask.setObjectName("radioButtonTask")
        self.radioButtonTime = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonTime.setGeometry(QtCore.QRect(20, 70, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButtonTime.setFont(font)
        self.radioButtonTime.setObjectName("radioButtonTime")
        self.taskCounter = QtWidgets.QSpinBox(self.groupBox)
        self.taskCounter.setGeometry(QtCore.QRect(280, 40, 91, 22))
        self.taskCounter.setStyleSheet("background-color: rgb(243, 168, 112);")
        self.taskCounter.setMaximum(1000000)
        self.taskCounter.setSingleStep(10)
        self.taskCounter.setProperty("value", 1000)
        self.taskCounter.setObjectName("taskCounter")
        self.timeCounter = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.timeCounter.setEnabled(False)
        self.timeCounter.setGeometry(QtCore.QRect(280, 70, 91, 22))
        self.timeCounter.setStyleSheet("background-color: rgb(243, 168, 112);")
        self.timeCounter.setMaximum(9999999999.99)
        self.timeCounter.setSingleStep(500.0)
        self.timeCounter.setProperty("value", 1000.0)
        self.timeCounter.setObjectName("timeCounter")
        self.deviceCount = QtWidgets.QSpinBox(self.centralwidget)
        self.deviceCount.setGeometry(QtCore.QRect(440, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.deviceCount.setFont(font)
        self.deviceCount.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.deviceCount.setMaximum(10)
        self.deviceCount.setProperty("value", 5)
        self.deviceCount.setObjectName("deviceCount")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(160, 60, 141, 141))
        self.widget_5.setStyleSheet("border-image: url(:/images/coin_money_finance_payment_icon.png);")
        self.widget_5.setObjectName("widget_5")
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setGeometry(QtCore.QRect(200, 200, 71, 101))
        self.widget_7.setStyleSheet("border-image: url(:/images/oie.png) 0 0 0 0 stretch stretch;")
        self.widget_7.setObjectName("widget_7")
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setGeometry(QtCore.QRect(180, 300, 111, 101))
        self.widget_8.setStyleSheet("border-image: url(:/images/trash_garbage_can_bin_ecology_icon.png) 0 0 0 0 stretch stretch;")
        self.widget_8.setObjectName("widget_8")
        self.queueSize = QtWidgets.QSpinBox(self.centralwidget)
        self.queueSize.setGeometry(QtCore.QRect(160, 30, 91, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        self.queueSize.setFont(font)
        self.queueSize.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.queueSize.setMaximum(1000)
        self.queueSize.setProperty("value", 34)
        self.queueSize.setObjectName("queueSize")
        self.widget_9 = QtWidgets.QWidget(self.centralwidget)
        self.widget_9.setGeometry(QtCore.QRect(300, 90, 141, 81))
        self.widget_9.setStyleSheet("border-image: url(:/images/arrow_right_next_forward_icon.png) 0 0 0 0 stretch stretch;")
        self.widget_9.setObjectName("widget_9")
        self.middleProcTime = QtWidgets.QLineEdit(self.widget_9)
        self.middleProcTime.setGeometry(QtCore.QRect(0, 27, 81, 27))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.middleProcTime.setFont(font)
        self.middleProcTime.setWhatsThis("")
        self.middleProcTime.setStyleSheet("border-image: none;\n"
"background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.middleProcTime.setObjectName("middleProcTime")
        self.widget_10 = QtWidgets.QWidget(self.centralwidget)
        self.widget_10.setGeometry(QtCore.QRect(580, 90, 151, 81))
        self.widget_10.setStyleSheet("border-image: url(:/images/arrow_right_next_forward_icon.png) 0 0 0 0 stretch stretch;")
        self.widget_10.setObjectName("widget_10")
        self.garbage = QtWidgets.QLabel(self.centralwidget)
        self.garbage.setGeometry(QtCore.QRect(184, 410, 111, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.garbage.setFont(font)
        self.garbage.setStyleSheet("color: rgb(37, 56, 144);")
        self.garbage.setObjectName("garbage")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 640, 571, 91))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.barGraph = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.barGraph.setEnabled(False)
        self.barGraph.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.barGraph.setObjectName("barGraph")
        self.horizontalLayout.addWidget(self.barGraph)
        self.scatter = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.scatter.setEnabled(False)
        self.scatter.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.scatter.setObjectName("scatter")
        self.horizontalLayout.addWidget(self.scatter)
        self.correlation = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.correlation.setEnabled(False)
        self.correlation.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.correlation.setObjectName("correlation")
        self.horizontalLayout.addWidget(self.correlation)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setStyleSheet("color: rgb(37, 56, 144);")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setStyleSheet("color: rgb(37, 56, 144);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setStyleSheet("color: rgb(37, 56, 144);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelExpectValue = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelExpectValue.setFont(font)
        self.labelExpectValue.setStyleSheet("color: rgb(37, 56, 144);")
        self.labelExpectValue.setText("")
        self.labelExpectValue.setAlignment(QtCore.Qt.AlignCenter)
        self.labelExpectValue.setObjectName("labelExpectValue")
        self.horizontalLayout_3.addWidget(self.labelExpectValue)
        self.labelDisp = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelDisp.setFont(font)
        self.labelDisp.setStyleSheet("color: rgb(37, 56, 144);")
        self.labelDisp.setText("")
        self.labelDisp.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDisp.setObjectName("labelDisp")
        self.horizontalLayout_3.addWidget(self.labelDisp)
        self.labelContInt = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelContInt.setFont(font)
        self.labelContInt.setStyleSheet("color: rgb(37, 56, 144);")
        self.labelContInt.setText("")
        self.labelContInt.setAlignment(QtCore.Qt.AlignCenter)
        self.labelContInt.setObjectName("labelContInt")
        self.horizontalLayout_3.addWidget(self.labelContInt)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.allTasks = QtWidgets.QLabel(self.centralwidget)
        self.allTasks.setGeometry(QtCore.QRect(20, 170, 141, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.allTasks.setFont(font)
        self.allTasks.setStyleSheet("color: rgb(37, 56, 144);")
        self.allTasks.setObjectName("allTasks")
        self.readyTasks = QtWidgets.QLabel(self.centralwidget)
        self.readyTasks.setGeometry(QtCore.QRect(590, 180, 131, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.readyTasks.setFont(font)
        self.readyTasks.setStyleSheet("color: rgb(37, 56, 144);")
        self.readyTasks.setObjectName("readyTasks")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(800, 30, 151, 471))
        self.tableWidget.setStyleSheet("color: rgb(37, 56, 144);")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 500, 571, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.barGraph_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.barGraph_2.setEnabled(False)
        self.barGraph_2.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.barGraph_2.setObjectName("barGraph_2")
        self.horizontalLayout_4.addWidget(self.barGraph_2)
        self.scatter_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.scatter_2.setEnabled(False)
        self.scatter_2.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.scatter_2.setObjectName("scatter_2")
        self.horizontalLayout_4.addWidget(self.scatter_2)
        self.correlation_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.correlation_2.setEnabled(False)
        self.correlation_2.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.correlation_2.setObjectName("correlation_2")
        self.horizontalLayout_4.addWidget(self.correlation_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setStyleSheet("color: rgb(37, 56, 144);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_5.setStyleSheet("color: rgb(37, 56, 144);")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_4.setStyleSheet("color: rgb(37, 56, 144);")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.labelExpectValue_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelExpectValue_2.setFont(font)
        self.labelExpectValue_2.setStyleSheet("color: rgb(37, 56, 144);")
        self.labelExpectValue_2.setText("")
        self.labelExpectValue_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelExpectValue_2.setObjectName("labelExpectValue_2")
        self.horizontalLayout_6.addWidget(self.labelExpectValue_2)
        self.labelDisp_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelDisp_2.setFont(font)
        self.labelDisp_2.setStyleSheet("color: rgb(37, 56, 144);")
        self.labelDisp_2.setText("")
        self.labelDisp_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDisp_2.setObjectName("labelDisp_2")
        self.horizontalLayout_6.addWidget(self.labelDisp_2)
        self.labelContInt_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.labelContInt_2.setFont(font)
        self.labelContInt_2.setStyleSheet("color: rgb(37, 56, 144);")
        self.labelContInt_2.setText("")
        self.labelContInt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelContInt_2.setObjectName("labelContInt_2")
        self.horizontalLayout_6.addWidget(self.labelContInt_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(950, 30, 151, 471))
        self.tableWidget_2.setStyleSheet("color: rgb(37, 56, 144);")
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 610, 221, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(37, 56, 144);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 470, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(37, 56, 144);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(720, 670, 462, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_7.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setStyleSheet("background-color: rgb(243, 168, 112);\n"
"color: rgb(37, 56, 144);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_7.addWidget(self.pushButton_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Система массового обслуживания"))
        self.startButton.setText(_translate("MainWindow", "Запуск моделирования"))
        self.middleArrivalTime.setText(_translate("MainWindow", "10"))
        self.groupBox.setTitle(_translate("MainWindow", "Условие остановки"))
        self.radioButtonTask.setText(_translate("MainWindow", "Количество заявок"))
        self.radioButtonTime.setText(_translate("MainWindow", "Время моделирования"))
        self.middleProcTime.setText(_translate("MainWindow", "25"))
        self.garbage.setText(_translate("MainWindow", "Отказов:  "))
        self.barGraph.setText(_translate("MainWindow", "Гистограмма"))
        self.scatter.setText(_translate("MainWindow", "График рассеивания"))
        self.correlation.setText(_translate("MainWindow", "График корреляции"))
        self.label_6.setText(_translate("MainWindow", "Математическое ожидание"))
        self.label_7.setText(_translate("MainWindow", "Дисперсия"))
        self.label_8.setText(_translate("MainWindow", "Доверительный интервал"))
        self.allTasks.setText(_translate("MainWindow", "Всего:"))
        self.readyTasks.setText(_translate("MainWindow", "Обработано: "))
        self.barGraph_2.setText(_translate("MainWindow", "Гистограмма"))
        self.scatter_2.setText(_translate("MainWindow", "График рассеивания"))
        self.correlation_2.setText(_translate("MainWindow", "График корреляции"))
        self.label_3.setText(_translate("MainWindow", "Математическое ожидание"))
        self.label_5.setText(_translate("MainWindow", "Дисперсия"))
        self.label_4.setText(_translate("MainWindow", "Доверительный интервал"))
        self.label.setText(_translate("MainWindow", "Для времени поступления"))
        self.label_2.setText(_translate("MainWindow", "Для времени обработки"))
        self.pushButton.setText(_translate("MainWindow", "Загруженность системы"))
        self.pushButton_2.setText(_translate("MainWindow", "Количество заявок"))
        self.pushButton_3.setText(_translate("MainWindow", "Среднее количество заявок"))
import icons