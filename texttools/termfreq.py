# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 16:56:54 2015

@author: Stephen Bishop
"""

from __future__ import division
from texttools import preprocess as make
import pandas as pd
from nltk import FreqDist


def termfreq(storytext, filename):
    '''
    This function takes a speech/text/article, preprocesses it into tokens, 
    removes stopwords, and outputs a csv of term counts and frequencies 
    relative to the size of the speech/text/article
    '''
    
    # Split into tokens, remove stopwords
    tokens = make.preprocess(storytext)
    stops = make.filter_stopwords(tokens)
    numstops = len(stops)    
    
    # Create a FreqDist and turn it into a list of tuples
    freq = FreqDist(stops)
    data = freq.items()[:numstops]
    
    # Build a pandas DataFrame of that list
    df = pd.DataFrame(data)
    df.columns = ['word', 'count']
    
    # Add a 'relative frequency' column to the DataFrame
    a = []
    for i in df['count']:
        a.append(i/numstops)
    df['pct'] = a
    
    # Write the file to csv
    df.to_csv('%s.csv' % filename, sep=',')
    print df
    print 'Check your files for the csv!'    

def tokencount(storytext):
    '''
    This function takes a speech/text/article, preprocesses it into tokens, 
    then outputs the number of tokens as an estimate for the total wordcount
    '''
    
    # Split into tokens, remove stopwords
    tokens = make.preprocess(storytext)
    length = len(tokens)
    
    # Write the integer to a .txt file
    f = open('totaltokencount.txt', 'w')
    f.write('%d' % length)
    f.close()   
    print  '%d tokens' % length