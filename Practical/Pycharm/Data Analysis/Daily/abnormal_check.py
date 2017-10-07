# _*_ encoding:utf-8 _*_
__author__ = 'lifan'
__date__ = '06/10/2017 22:33'

import pandas as pd
import matplotlib.pyplot as plt

catering_sale = '../data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')

plt.rcParams['font.sans-serif'] = ['SimHei']  # to display Chinese label
plt.rcParams['axes.unicode_minus'] = False

plt.figure()
p = data.boxplot(return_type='dict')
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort()

for i in range(len(x)):
    if i > 0:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.05 - 0.8 / (y[i] - y[i - 1]), y[i]))
    else:
        plt.annotate(y[i], xy=(x[i], y[i]), xytext=(x[i] + 0.08, y[i]))

plt.show()
