from main import main
from estimates import *
import numpy as np
import openpyxl
from distributions import *


def N():
    result_table = []
    change_elem()
    for i in range(200):
        create_list(2000)
        dictionary1, que1, dev1 = main(2000, 0)
        change_list()
        dictionary2, que2, dev2 = main(2000, 0)
        print(i)
        # print(i, dictionary1['Tq'], dictionary2['Tq'], (dictionary1['Tq'] + dictionary2['Tq']) / 2)

        result_table.append([(dictionary1['p'] + dictionary2['p']) / 2, (dictionary1['Tq'] + dictionary2['Tq']) / 2,
                            (dictionary1['Ts'] + dictionary2['Ts']) / 2, (dictionary1['Nq'] + dictionary2['Nq']) / 2,
                            (dictionary1['Ns'] + dictionary2['Ns']) / 2, (dictionary1['Ca'] + dictionary2['Ca']) / 2,
                            (dictionary1['Cr'] + dictionary2['Cr']) / 2])
    m = []
    d = []
    for i in range(7):
        temp = []
        for j in range(len(result_table)):
            temp.append(result_table[j][i])
        t1, t2 = estimates(temp)
        m.append(t1)
        d.append(t2)
    result_table.append(m)
    result_table.append(d)
    eps = [i * 0.05 for i in m]
    result_table.append(eps)
    u = 1.96
    result_table.append([u ** 2 * d[i] / eps[i] ** 2 for i in range(7)])

    wb = openpyxl.Workbook()
    wb.create_sheet(title='Первый лист', index=0)
    sheet = wb['Первый лист']
    sheet.append(result_table[len(result_table) - 4])
    sheet.append(result_table[len(result_table) - 3])
    sheet.append(result_table[len(result_table) - 2])
    sheet.append(result_table[len(result_table) - 1])
    wb.save('n.xlsx')


N()
