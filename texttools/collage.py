# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 20:02:25 2015

@author: Stephen Bishop
"""

import preprocess as make

def collage(storytext, n=None, prints=None):
    '''
    This is the main function. Call this function to output everything I need
    to make a concordance collage     
    '''    
    tokens = make.preprocess(storytext, prints)
    remstop = make.filter_stopwords(tokens, prints)
    frequ = make.freq(remstop, n, prints)
    make.concordance_list(frequ, tokens, n) 