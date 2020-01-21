from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from form import Ui_MainWindow
from main import main
from estimates import *
import sys


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.btn_start_clicked)
        self.ui.barGraph.clicked.connect(self.btn_bar_graph_clicked)
        self.ui.correlation.clicked.connect(self.btn_correlation_clicked)
        self.ui.scatter.clicked.connect(self.btn_scatter_clicked)
        self.ui.barGraph_2.clicked.connect(self.btn_bar_graph_2_clicked)
        self.ui.correlation_2.clicked.connect(self.btn_correlation_2_clicked)
        self.ui.scatter_2.clicked.connect(self.btn_scatter_2_clicked)
        self.ui.radioButtonTask.toggled.connect(self.change_radio_btn)
        self.ui.radioButtonTask.toggled.connect(self.change_radio_btn)
        self.ui.pushButton_2.clicked.connect(self.plots)
        self.ui.pushButton_3.clicked.connect(self.avr_plots)
        self.ui.pushButton.clicked.connect(self.coefficient_plots)

    def btn_start_clicked(self):

        queue_size = int(self.ui.queueSize.text())
        devices = int(self.ui.deviceCount.text())
        process_time = float(self.ui.middleProcTime.text())
        arrival_time = float(self.ui.middleArrivalTime.text())
        if self.ui.radioButtonTask.isChecked():
            finish_condition = int(self.ui.taskCounter.text())
            sys_state = 2
        else:
            finish_condition = float(self.ui.timeCounter.text().replace(',', '.'))
            sys_state = 1

        if queue_size > 0 and devices > 0 and process_time > 0 and arrival_time > 0 and finish_condition > 0:
            ans, self.que, self.dev = main(finish_condition, sys_state, devices, queue_size, process_time, arrival_time)
            for i in range(len(self.que.exp_dist_arrive)-1, 1, -1):
                self.que.exp_dist_arrive[i] -= self.que.exp_dist_arrive[i-1]
            self.ui.barGraph.setEnabled(True)
            self.ui.correlation.setEnabled(True)
            self.ui.scatter.setEnabled(True)

            self.ui.barGraph_2.setEnabled(True)
            self.ui.correlation_2.setEnabled(True)
            self.ui.scatter_2.setEnabled(True)

            self.ui.pushButton.setEnabled(True)
            self.ui.pushButton_2.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)

            self.ui.allTasks.setText('Всего: \n' + str(self.que.all_tasks))
            self.ui.garbage.setText('Отказов: \n' + str(self.que.fail))
            self.ui.readyTasks.setText('Обработано: \n' + str(self.que.ready))
            self.create_table_dev(ans['devices'])
            self.create_table_info([ans['p'], ans['Ns'], ans['Nq'], ans['Tq'], ans['Ts'], ans['Ca'], ans['Cr']])

            m, d = estimates(self.que.exp_dist_arrive)
            self.ui.labelDisp.setText('= ' + str(d))
            self.ui.labelExpectValue.setText('= ' + str(m))
            self.ui.labelContInt.setText(confidence_interval(m, d, arrival_time, len(self.que.exp_dist_arrive)))

            m, d = estimates(self.que.exp_dist_prc)
            self.ui.labelDisp_2.setText('= ' + str(d))
            self.ui.labelExpectValue_2.setText('= ' + str(m))
            self.ui.labelContInt_2.setText(confidence_interval(m, d, process_time, len(self.que.exp_dist_prc)))

    def create_table_dev(self, devices):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setRowCount(len(devices))
        self.ui.tableWidget.setColumnCount(1)
        for i in range(len(devices)):
            progress = QtWidgets.QProgressBar()
            progress.setMinimum(0)
            progress.setMaximum(100)

            progress.setValue(min(devices[i], 100))
            progress.setFormat('{0:.2f}%'.format(devices[i]))
            progress.setAlignment(Qt.AlignCenter)
            progress.setStyleSheet("""QProgressBar::chunk { 
            border: 2px solid rgb(36,53,129);
            background-color: lightblue; }""")

            self.ui.tableWidget.setCellWidget(i, 0, progress)
        self.ui.tableWidget.setHorizontalHeaderLabels(['Устройства'])

    def create_table_info(self, ans):
        self.ui.tableWidget_2.clear()
        self.ui.tableWidget_2.setRowCount(7)
        self.ui.tableWidget_2.setColumnCount(1)
        for i in range(7):
            self.ui.tableWidget_2.setItem(i, 0, QTableWidgetItem(str(ans[i])))
        self.ui.tableWidget_2.setHorizontalHeaderLabels(['Отклики'])
        self.ui.tableWidget_2.setVerticalHeaderLabels(('p', 'Ns', 'Nq', 'Tq', 'Ts', 'Ca', 'Cr'))

    def btn_bar_graph_clicked(self):
        bar_graph(self.que.exp_dist_arrive, float(self.ui.middleArrivalTime.text()))

    def btn_correlation_clicked(self):
        m, d = estimates(self.que.exp_dist_arrive)
        correlation(self.que.exp_dist_arrive, m, d)

    def btn_scatter_clicked(self):
        scatter_plot(self.que.exp_dist_arrive)

    def btn_bar_graph_2_clicked(self):
        bar_graph(self.que.exp_dist_prc, float(self.ui.middleProcTime.text()))

    def btn_correlation_2_clicked(self):
        m, d = estimates(self.que.exp_dist_arrive)
        correlation(self.que.exp_dist_prc, m, d)

    def btn_scatter_2_clicked(self):
        scatter_plot(self.que.exp_dist_prc)

    def change_radio_btn(self):
        if self.ui.radioButtonTask.isChecked():
            self.ui.taskCounter.setEnabled(True)
            self.ui.timeCounter.setEnabled(False)
        else:
            self.ui.taskCounter.setEnabled(False)
            self.ui.timeCounter.setEnabled(True)

    def plots(self):
        figure, (ax1, ax2) = plt.subplots(2, 1)
        ax1.plot(self.que.cur_task_in_queue, color='#f3a870')
        ax1.set_title('Количество заявок в очереди')
        ax2.plot([self.que.cur_task_in_queue[i] + self.dev.cur_task_in_dev[i]
                  for i in range(len(self.que.cur_task_in_queue))], color='#243580')
        ax2.set_title('Количество заявок в системе')
        plt.show()

    def avr_plots(self):
        figure, (ax1, ax2) = plt.subplots(2, 1)
        ax1.plot(self.que.avr_cur_task_in_queue, color='#f3a870')
        ax1.set_title('Среднее количество заявок в очереди')
        ax2.plot([self.que.avr_cur_task_in_queue[i] + self.dev.avr_cur_task_in_dev[i]
                  for i in range(len(self.que.avr_cur_task_in_queue))], color='#243580')
        ax2.set_title('Среднее количество заявок в системе')
        plt.show()

    def coefficient_plots(self):
        figure, ax = plt.subplots(1, 1)
        ax.plot(self.dev.coefficients_dev, color='#eb5967')
        ax.set_title('Коэффициент использования системы')
        plt.show()


app = QtWidgets.QApplication([])
application = Window()
application.show()
sys.exit(app.exec())
