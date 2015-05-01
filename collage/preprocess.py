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

def preprocess(text):
     '''
     This function takes a string of the text and returns a list of tokens
     built from the given text
     '''
     text = text.lower()
     tokenizer = RegexpTokenizer(r'\w+')
     tokens = tokenizer.tokenize(text)
     print tokens[0:20]
     return tokens
 
 
def filter_stopwords(tokens):
    '''
    This function takes a list of tokens and removes the stopwords,
    returning a list of removed stopwords and printing the first 20 words
    '''
    
    stop = stopwords.words('english')
    remstop = [i for i in tokens if i not in stop]
    print 'LIST OF TOKENS WITHOUT STOPWORDS'    
    print remstop[0:20]
    return remstop

def freq(tokens, n=None):
    '''
    This function takes a list of tokens and returns a list of the top n most 
    frequent tokens
    
    It also prints a frequency distribution of the top 50 tokens
    '''
    fdist2 = FreqDist(tokens)
    fdist2.plot(50, cumulative=True)
    if n is None:    
        print fdist2.items()[:20]
        return fdist2.items()[:20]
    else:
        print fdist2.items()[:n]
        return fdist2.items()[:n]


def concordance_list(listofwords, n=None):
    '''
    This function takes a list of words and outputstheir concordance outputs.
    
    If n is given, it will only print the first n numbers in the list
    '''    
    
    if n is None:
        n = len(listofwords)
    mylist = listofwords[:n]
    SpeechText = nltk.Text(mylist)    
    if n is None:
        for i in mylist[:n]:
            print SpeechText.concordance(i, lines=50)
    else:
        for i in mylist[:10]:
            print SpeechText.concordance(i, lines=50)


def collage(storytext, n=None):
    '''
    This is the main function. Call this function to output everything I need
    to make a concordance collage     
    '''
    tokens = preprocess(storytext)
    remstop = filter_stopwords(tokens)
    frequ = freq(remstop)
    concordance_list(remstop)
    
