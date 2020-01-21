# -*- coding: utf-8 -*-
from scipy.stats import expon, chisquare, chi2
from numpy import arange
from math import exp
import matplotlib.pyplot as plt


def estimates(dist):
    n = len(dist)
    # Мат ожидание
    m = round(sum(dist) / n, 2)

    # Дисперсия
    d = round(sum([(i - m) ** 2 for i in dist]) / (n - 1), 2)
    return m, d


def scatter_plot(dist):
    figure, ax = plt.subplots(1, 1)
    # Рассеивание
    n = len(dist)
    for i in range(1, min(1000, n)):
        ax.scatter(dist[i], dist[i - 1], marker='o', c='#eb5967')
    ax.grid()
    plt.show()


def correlation(dist, m, d):
    figure, ax = plt.subplots(1, 1)
    # Корреляция
    n = len(dist)
    max_j = 20
    k = [0] * max_j
    for j in range(1, max_j):
        k[j] = sum([(dist[i] - m) * (dist[i + j] - m) for i in range(n-j)]) / (n-j)
        # for i in xrange(n-j):
        #     k[j] += (dist[i] - m) * (dist[i + j] - m)
        # k[j] /= (n - j)

    # Коэффициент корреляции
    p = [float(elem)/d for elem in k]
    # График корреляции
    ax.scatter(range(max_j), p, marker='x', c='#f3a870')
    ax.grid()
    plt.show()


def bar_graph(dist, mu):
    figure, ax = plt.subplots(1, 1)
    # Гистограмма
    n = len(dist)
    minim = min(dist)
    maxim = max(dist)
    count_of_interval = round(1.72 * (n ** (1/3)))
    x = (maxim - minim) / float(count_of_interval)
    h = [0]*count_of_interval
    for i in range(n):
        for j in range(1, count_of_interval):
            if x * j >= dist[i] >= x * (j - 1):
                h[j - 1] += 1
                break

    hi = [step for step in arange(minim, maxim + x, x)]
    e = [(expon.cdf(hi[i], loc=0, scale=mu) - expon.cdf(hi[i - 1], loc=0, scale=mu)) * n for i in range(1, len(hi))]
    hi_square = chisquare(h[:min(len(h), len(e))], e[:min(len(h), len(e))], ddof=1)

    for j in range(5):
        for i in range(len(h)):
            if i >= len(h):
                break
            if h[i] <= 5:
                h[i - 1] += h[i]
                del h[i]
                count_of_interval -= 1
                i = 0
    print(count_of_interval)
    for j in range(1, count_of_interval+1):
        print(x*(j-1), x * j)

    # print(h)
    # print(e)
    ax.hist(dist, density=True, bins=count_of_interval, edgecolor='black')

    f_exp = [1 / mu * exp(-value_x / mu) for value_x in range(0, int(max(dist)))]
    ax.plot(range(0, int(max(dist))), f_exp, c='#f3a870')

    # ax.text(count_of_interval - count_of_interval / 2, 1 / float(mu) - 1 / float(mu) / 2,
    #         'hi2 = ' + str(round(hi_square[0], 2)) + ' < ' + str(round(chi2.ppf(0.95, df=count_of_interval - 1), 2)),
    #         fontsize=16, c='#f3a870')

    # print(round(hi_square[0], 2), round(chi2.ppf(0.95, df=count_of_interval - 1), 2))
    plt.show()


def confidence_interval(m, d, expected_m, n):
    # Доверительный интервал
    u = 1.96
    sigma = d**0.5
    left = round(m - (sigma * u) / (n**0.5), 2)
    right = round(m + (sigma * u) / (n**0.5), 2)
    return str(left) + ' < ' + str(expected_m) + ' < ' + str(right)
