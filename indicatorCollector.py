import sys
import pandas as pd
import requests
import json
import numpy as np
import datetime
from dateutil.parser import parse




def getRsi(tickerId, date):
    request_url = "https://www.alphavantage.co/query?function=RSI&symbol="+tickerId+"&interval=15min&time_period=200&series_type=close&apikey=1ILVVLJ4BTJJWQB3"
    request = requests.get(requests_url)
    results = json.loads(request.text)
    return results["Technical Analysis: RSI"][date[0:16]]["RSI"]
#end date ex "2018-11-02 16:00:00"
def priceChange(tickerId, date):
    request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+tickerId+"&interval=15min&outputsize=full&apikey=1ILVVLJ4BTJJWQB3"
    startRequest = requests.get(request_url)
    startResult = json.loads(startRequest.text)
    print(startResult)

    startPrice = float(startResult[date]["4. close"])
    endPrice = float(startResult[date[0:11]+"16:00:00"]["4. close"])

    return ((startPrice - endPrice)/startPrice)

def getStoch(tickerId, date):
    request_url = "https://www.alphavantage.co/query?function=STOCH&symbol="+tickerId+"&interval=15min&apikey=1ILVVLJ4BTJJWQB3"
    request = requests.get(request_url)
    results = json.loads(request.text)
    return results["Technical Analysis: STOCH"][date[0:16]]

def adx(tickerId, date):
    request_url = "https://www.alphavantage.co/query?function=ADX&symbol="+tickerId+"&interval=15min&time_period=10&apikey=1ILVVLJ4BTJJWQB3"
    request = requests.get(request_url)
    results = json.loads(request.text)
    return results["Technical Analysis: ADX"][date[0:16]]["ADX"]

def aroon(tickerId, date):
    request_url = "https://www.alphavantage.co/query?function=AROON&symbol="+tickerId+"&interval=15min&time_period=14&apikey=1ILVVLJ4BTJJWQB3"
    request = requests.get(request_url)
    results = json.loads(request.text)
    return results["Technical Analysis: AROON"][date[0:16]]

def obv(tickerId, date):
    request_url = "https://www.alphavantage.co/query?function=OBV&symbol="+tickerId+"&interval=15min&apikey=1ILVVLJ4BTJJWQB3"
    request = requests.get(request_url)
    results = json.loads(request.text)
    return results["Technical Analysis: OBV"][date[0:16]]["OBV"]

def ad(tickerId, date):
    request_url = "https://www.alphavantage.co/query?function=AD&symbol="+tickerId+"&interval=15min&apikey=1ILVVLJ4BTJJWQB3"
    request = requests.get(request_url)
    results = json.loads(request.text)
    return results["Technical Analysis: Chaikin A/D"][date[0:16]]["Chaikin A/D"]



#change in price >= threshold for this to work
def main():
    filename = sys.argv[1]
    unpicked_df = pd.read_pickle("./" + str(filename))
    compiledDict = {"ad": [], "obv":[], "aroon up":[]
    , "aroon down":[],"adx":[],"stoch":[], "priceChange":[],"rsi":[]}

    for index in range(len(unpicked_df)):
        tm = datetime.datetime.strptime(unpicked_df["time"][index], "%Y-%m-%d %H:%M:%S")
        discard = datetime.timedelta(minutes=tm.minute % 15, seconds=tm.second, microseconds=tm.microsecond)
        tm -= discard
        if discard >= datetime.timedelta(minutes=7):
            tm += datetime.timedelta(minutes=15)
        #now tm is equal to the time rounded to the nearest 15 minutes
        tm = str(tm)

        #compiledDict["ad"].append(int(ad(unpicked_df["ticker"][index], tm)))
        compiledDict["obv"].append(obv(unpicked_df["ticker"][index], tm))
        print("ran")
        compiledDict["aroon up"].append(aroon(unpicked_df["ticker"][index], tm)["Aroon Up"])

        compiledDict["aroon down"].append(aroon(unpicked_df["ticker"][index], tm)["Aroon Down"])
        compiledDict["adx"].append(adx(unpicked_df["ticker"][index], tm))
        compiledDict["stoch"].append(getStoch(unpicked_df["ticker"][index], tm))
        compiledDict["priceChange"].append(priceChange(unpicked_df["ticker"][index], tm))
        compiledDict["rsi"].append(getRsi(unpicked_df["ticker"][index], tm))

    indicators_df = pd.DataFrame.from_dict(compiledDict)
    result = pd.concat([unpicked_df, indicators_df], axis = 1)

    result.to_pickle("./indicators.pkl")


if __name__== "__main__":
    main()


