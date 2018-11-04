# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 01:30:36 2018

@author: Abhishek
"""

import textblob as tb

def analyze(text, company, companyTickersSet, companyNamesSet):
    analysis = {}

    blob = tb.TextBlob(text)
    analysis['polarity'] = blob.sentiment[0]
    analysis['subjectivity'] = blob.sentiment[1]
    analysis['wordCount'] = len(blob.words)
    analysis['sentenceCount'] = len(blob.sentences)

    analysis['companyMentions'] = 0
    analysis['firstSentenceMentioned'] = 0

    thisTextCompanySet = set()
    found = False

    for i in range(len(blob.sentences)):
        for word in blob.sentences[i]:
            if word in companyTickersSet or word in companyNamesSet:
                thisTextCompanySet.add(word)

            if(word == company['name'] or word == company['ticker']):
                analysis['companyMentions'] += 1
                if(not found):
                    analysis['firstSentenceMentioned'] = i
                    found = True


        analysis['companiesMentioned'] = len(thisTextCompanySet)


    return analysis

