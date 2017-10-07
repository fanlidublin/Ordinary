# _*_ encoding:utf-8 _*_
from __future__ import print_function

__author__ = 'lifan'
__date__ = '07/10/2017 22:14'

import pandas as pd

catering_sale = '../data/catering_sale.xls'
data = pd.read_excel(catering_sale, index_col=u'日期')
# filter the data
data = data[(data[u'销售'] > 400) & (data[u'销售'] < 5000)]
statistics = data.describe()

statistics.loc['range'] = statistics.loc['max'] - statistics['min']
statistics.loc['var'] = statistics.loc['std'] / statistics.loc['mean']
statistics.loc['dis'] = statistics.loc['75%'] - statistics.loc['25%']

print(statistics)
