# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:37:16 2015

@author: Stephen Bishop
"""

import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from nltk import FreqDist

storytext = open("wheredowego.txt").read()

# Function to preprocess words into tokens
def preprocess(sentence):
     sentence = sentence.lower()
     tokenizer = RegexpTokenizer(r'\w+')
     tokens = tokenizer.tokenize(sentence)
     print tokens[0:20]
     return tokens
 
 
def filter_stopwords(tokens):
    stop = stopwords.words('english')
    remstop = [i for i in tokens if i not in stop]
    print remstop[0:20]
    return remstop

def freq(remstop):
    fdist2 = FreqDist(remstop)
    x = fdist2.items()[:20]
    fdist2.plot(50, cumulative=True)

def concordance_list(listofwords, n=None):
    if n is None:
        n = len(listofwords)
    mylist = listofwords[:n]
    SpeechText = nltk.Text(tokens)    
    for i in mylist:
        print SpeechText.concordance(i, lines=50)



concordance_list(stop)
preprocessedStory = preprocess(storytext)
tokens = nltk.word_tokenize(preprocessedStory)
print tokens[0:20]
len(tokens)


stop = stopwords.words('english')
remstop = [i for i in tokens if i not in stop]
remstop[0:20]
len(remstop)

# Turn it into an nltk text object
SpeechText = nltk.Text(tokens)
SpeechText.concordance('power', lines=47)
SpeechText.concordance('dissatisfied', lines=38)
SpeechText.concordance('negroes', lines=38)
SpeechText.concordance('negro', lines=38)
SpeechText.concordance('negroes', lines=38)
SpeechText.concordance('struggle', lines=38)
SpeechText.concordance('justice', lines=38)
SpeechText.concordance('problems', lines=38)
SpeechText.concordance('freedom', lines=38)
SpeechText.concordance('rights', lines=38)