import requests
import json
import sys
import pandas as pd
import datetime
import pickle
import os.path

def main():
    filename = sys.argv[1]
    #df = pd.read_pickle("./" + str(filename))
    tickers = 0
    with open("tickers.pkl", "rb") as file:
        tickers = pickle.load(file)
    for ticker in tickers:


        if not os.path.exists(ticker + ".pkl"):
            try:
                dictionary = {}

                for i in range(3, 31):
                    date = "201810" + str(i)
                    print(ticker)
                    print(date)
                    r = requests.get('https://api.iextrading.com/1.0/stock/' + ticker + '/chart/date/' + date)
                    dictionary[date] = r.json()
                with open(ticker + ".pkl", "wb") as tmp:
                    pickle.dump(dictionary, tmp)
            except:
                print(ticker+" Failed")
        else:
            print(ticker+ " File already exists")





if __name__== "__main__":
    main()