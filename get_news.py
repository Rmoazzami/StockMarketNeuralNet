import pickle
import pandas as pd
from eventregistry import *

sandp = pd.read_csv('sandp500.csv')
companies = sandp.values
all_articles = []
#skipped 248-258
base = 357
basePlus100 = base + 99
for i, company in enumerate(companies[base:basePlus100]):
    company_ticker = company[0]
    company_name = company[1]
    print company_ticker
    print company_name
    er = EventRegistry(apiKey = "63071754-2d49-4533-b657-46be1b5481c9")

    q= QueryArticlesIter(
        conceptUri = er.getConceptUri(company_name),
        lang = ["eng"],
        sourceGroupUri = er.getSourceGroupUri("business ERtop25"))
    # obtain at most 500 newest articles or blog posts
    query = q.execQuery(er, sortBy = "date", maxItems = 500)

    articles = [art for art in query]
    for article in articles:
        article["company"] = company_name
        article["ticker"] = company_ticker
    all_articles.extend(articles)

with open('all_articles.pkl', 'wb') as fp:
    pickle.dump(all_articles, fp)

"""
with open ('all_articles.pkl', 'rb') as fp:
    all_articles = pickle.load(fp)

for article in all_articles:
    print article
    """



"""import requests
import json

url = ('https://newsapi.org/v2/everything?'
       'q=Apple&'
       'from=2018-10-03&'
       'sortBy=popularity&'
       'apiKey=1327b63246734ba58f31a5d4e03d5f6a')

response = requests.get(url)
"""
