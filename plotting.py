# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 19:20:47 2018

@author: Abhishek
"""

import plotly as py
import plotly.graph_objs as go

import pickle

from datetime import datetime
import pandas_datareader.data as web

def CompanyStats(company = 'AMZN', tradesDict = None):
# =============================================================================
#   Gives Stats on the company, as well as the trades
#     Args:
#         company (str)
#         tradesDict ({'buys': [], 'sells':[]}
# =============================================================================

    tradesDict = [ datetime(2018, 10, 12, 0, 13, 19),
 datetime(2018, 10, 12, 0, 13, 20),
 datetime(2018, 10, 12, 0, 13, 21),
 datetime(2018, 10, 12, 0, 13, 22),
 datetime(2018, 10, 12, 0, 13, 23),
 datetime(2018, 10, 12, 0, 13, 24)]
    with open (company + '.pkl', 'rb') as f:
        fileData = pickle.load(f)

    xvals = []
    prices = []

    xvals2 = []
    prices2 = []

    for day in fileData.keys():
        if len(fileData[day]) != 0:
            for m in fileData[day]:
                t = datetime.strptime(m['date']+m['minute'], '%Y%m%d%M:%S')
                if(t in tradesDict):
                    xvals2.append(t)
                    prices2.append(m['close'])

                if m['volume']:
                    xvals.append(t)
                    prices.append(m['close'])


    trace1 = go.Scatter(x=xvals, y=prices)
    trace2 = go.Scatter(x=xvals2, y=prices2, mode='markers', marker={'size':10})

    data = [trace1, trace2]
    layout = dict(
        title=company,
        xaxis=dict(
                rangeselector=dict(
                buttons=list([
                    dict(count=1,
                         label='1m',
                         step='month',
                         stepmode='backward'),
                    dict(count=6,
                         label='6m',
                         step='month',
                         stepmode='backward'),
                    dict(count=1,
                        label='YTD',
                        step='year',
                        stepmode='todate'),
                    dict(count=1,
                        label='1y',
                        step='year',
                        stepmode='backward'),
                    dict(step='all')
                ])
            ),
            rangeslider=dict(
                visible = True
            ),
            type='category'
        )
    )

    fig = dict(data=data, layout=layout)
    py.offline.plot(fig)



if __name__ == '__main__':
    CompanyStats()