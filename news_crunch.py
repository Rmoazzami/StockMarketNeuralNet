# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 11:36:53 2018

@author: Abhishek

"""
import pickle
import pandas as pd
from datetime import datetime

from analyze import analyze


articlesList= pd.read_pickle('all_articles4.pkl')
companyTickersSet= pd.read_pickle('companyTickers.pkl')
companyNamesSet= pd.read_pickle('companyNames.pkl')

keys = ('datetime', 'ticker', 'polarity', 'subjectivity', 'wordCount', 'sentenceCount', 'companyMentions', 'firstSentenceMentioned', 'companiesMentioned')
df = pd.DataFrame(columns = keys)
df = df.transpose()

for i, article in enumerate(articlesList):
    if(i % 3000 == 0):
        print(f'{i} articles processed at {datetime.now().time()}')
        df = df.transpose()
        df.to_pickle("articleAnalysis.pkl")
        df = df.transpose()

    company = article['company']
    ticker = article['ticker']
    contains = False

    for word in article['title']:
        if word in companyNamesSet or word in companyTickersSet:
            contains = True;
            break;

    if contains:
        companyDict = {'name': company, 'ticker': ticker}
        output = analyze(article['body'], companyDict, companyTickersSet, companyNamesSet)
        outputList = [article['dateTime'], ticker, output[keys[2]],
                      output[keys[3]], output[keys[4]], output[keys[5]],
                      output[keys[6]], output[keys[7]], output[keys[8]]]
        df[i] = outputList