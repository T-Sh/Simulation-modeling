# -*- coding: utf-8 -*-
from math import exp
from math import log
import random
import openpyxl

# cur_uni_elem = 1234567890
start_elem_1 = random.randint(1000000000, 1800000000)
start_elem_2 = random.randint(1000000000, 1800000000)
cur_uni_elem_1 = start_elem_1
cur_uni_elem_2 = start_elem_2

dist_list11 = []
dist_list12 = []
dist_list21 = []
dist_list22 = []

wb1 = openpyxl.Workbook()
wb1.create_sheet(title='1', index=0)
sheet1 = wb1['1']


def create_list(count=2000):
    global dist_list11, dist_list12, dist_list21, dist_list22
    dist_list11 = []
    dist_list12 = []
    dist_list21 = []
    dist_list22 = []
    for i in range(count):
        u1 = uni_dist_1()
        u2 = uni_dist_2()
        dist_list11.append(u1)
        dist_list12.append(u2)
        dist_list21.append(1-u1)
        dist_list22.append(1-u2)


def change_list():
    global dist_list11, dist_list12
    dist_list11 = dist_list21
    dist_list12 = dist_list22


def change_elem():
    global cur_uni_elem_1, cur_uni_elem_2
    cur_uni_elem_1 = start_elem_1
    cur_uni_elem_2 = start_elem_2
    table_append()


def random_elem():
    global cur_uni_elem_1, cur_uni_elem_2
    cur_uni_elem_1 = random.randint(1500000000, 2000000000)
    cur_uni_elem_2 = random.randint(1500000000, 2000000000)
    table_append()


def table_append():
    sheet1.append([cur_uni_elem_1, cur_uni_elem_2])


def save_table():
    wb1.save('Нач значения.xlsx')


def uni_dist_1():
    global cur_uni_elem_1
    a = 630360016
    m = 2147483647
    cur_uni_elem_1 = (a * cur_uni_elem_1) % m
    return float(cur_uni_elem_1) / m


def uni_dist_2():
    global cur_uni_elem_2
    a = 630360016
    m = 2147483647
    cur_uni_elem_2 = (a * cur_uni_elem_2) % m
    return float(cur_uni_elem_2) / m


def exp_dist(mu):
    # return -mu * log(uni_dist_1())
    return -mu * log(dist_list11.pop())


def exp_dist_proc(mu):
    # return -mu * log(uni_dist_2())
    return -mu * log(dist_list12.pop())

