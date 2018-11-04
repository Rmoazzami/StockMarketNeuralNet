# StockMarketNeuralNet
An Algorithm trader that utilized neural networks to asses the impacts of news articles and technical indicators on the price of the stock.

Created for the 2018 Vanderbilt Hackathon, the files aim to gather news data from API's and rate their sentiment and impact 
on the community and couple that with technical indicators (RSI, Bollinger Band, Stoch, Aroon up/down)
to feed into a neural network that is trained on the data 
(Started with 250,000 data points but due to most clean datasets being sold at a premium we were only able to gather a fraction of that cleanly)

The Neural Net's accuracy was 61.44% on some training runs as opposed to the 33% expected from a random classifier of postive, neutral, and negative prediction.

Note: All data points where exclusively for the month of october 2018
