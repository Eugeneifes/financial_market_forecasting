__author__ = 'Eugene'
# -*- coding: utf-8 -*-

from yahoo_finance import Share
import matplotlib.pyplot as plt
import csv
import pandas as pd

def Load_Data():
    yahoo = Share('MSFT')
    data = yahoo.get_historical('2014-01-01', '2015-01-01')
    with open('database.csv', 'w') as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


df = pd.read_csv('database.csv', index_col='Date')
high_px = df['High']
high_px = high_px.sort_index(ascending=True)
high_px.plot(label='Price')
plt.legend()
plt.show()
