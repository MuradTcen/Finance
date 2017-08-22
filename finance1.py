#  -*- coding: utf-8 -*-
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from stock2dict import *

style.use('ggplot')
'''
case for tsla stock
start = dt.datetime(2010, 1, 1)
end = dt.datetime(2016, 12, 31)
df = web.DataReader('TSLA', 'google', start, end)
'''

# '''
# case for mcx:magn stock
url = 'https://www.google.com/finance/historical?q=MAGN&startdate=Jan+01%2C+2010&enddate=Dec+31%2C+2016'
list = get_pages_data(get_html(url))
df = pd.DataFrame(
    list, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
df['Date'] = df['Date'].apply(lambda x: pd.to_datetime(x))
df = df.set_index('Date')
# '''

print(df.tail())
