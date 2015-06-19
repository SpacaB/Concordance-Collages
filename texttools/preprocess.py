# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 21:37:16 2015

@author: Stephen Bishop
"""

from __future__ import division
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from nltk import FreqDist

import pandas as pd

def preprocess(text, prints=None):
     '''
     This function takes a string of the text and returns a list of tokens
     built from the given text
     '''
     text = text.lower()
     tokenizer = RegexpTokenizer(r'\w+')
     tokens = tokenizer.tokenize(text)
     if prints is 'yes':
         print tokens[0:20]
     return tokens
 
def filter_stopwords(tokens, prints=None):
    '''
    This function takes a list of tokens and removes the stopwords,
    returning a list of removed stopwords and printing the first 20 words
    '''
    
    stop = stopwords.words('english')
    remstop = [i for i in tokens if i not in stop]
    if prints is 'yes':
        print 'LIST OF TOKENS WITHOUT STOPWORDS'    
        print remstop[0:20]
    return remstop

def freq(tokens, n=None, prints=None):
    '''
    This function takes a list of tokens and returns a list of the top n most 
    frequent tokens
    
    It also prints a frequency distribution of the top 50 tokens
    '''
    fdist2 = FreqDist(tokens)
    fdist2.plot(50, cumulative=True)
    [i[0] for i in fdist2.items()[:20]]
    if prints is 'yes':
        if n is None:    
            print fdist2.items()[:20]
            return [i[0] for i in fdist2.items()[:20]]
        else:
            print fdist2.items()[:n]
            return [i[0] for i in fdist2.items()[:n]]
    else:
        if n is None:
            return [i[0] for i in fdist2.items()[:20]]
        else:
            return [i[0] for i in fdist2.items()[:n]]


def concordance_list(listofwords, tokens, n=None):
    '''
    This function takes a list of words and outputstheir concordance outputs.
    
    If n is given, it will only print the first n numbers in the list
    '''    
    SpeechText = nltk.Text(tokens)
    if n is None:
        for i in listofwords[:10]:
            print SpeechText.concordance(i, lines=50)
    else:
        for i in listofwords[:n]:
            print SpeechText.concordance(i, lines=50)
