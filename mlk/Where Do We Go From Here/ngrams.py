# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:11:12 2015

@author: Stephen Bishop
"""

# This code is from some guy on StackOverflow

import nltk
import re
from nltk.tokenize import RegexpTokenizer
from nltk import bigrams
from nltk import trigrams
from nltk import ngrams

# split the texts into tokens
storytext = open("wheredowego.txt").read()


# Function to preprocess words into tokens
def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	return " ".join(tokens)

tokens = preprocess(storytext)
tokens = nltk.word_tokenize(tokens)
tokens = [token.lower() for token in tokens if len(token) > 1] #same as unigrams
bi_tokens = bigrams(tokens)
tri_tokens = trigrams(tokens)
fourgrams = ngrams(tokens, 4)

# print bigrams count
print [(item, bi_tokens.count(item)) for item in sorted(set(bi_tokens))]

# print trigrams count
print [(item, tri_tokens.count(item)) for item in sorted(set(tri_tokens))]

# Freqdist bigrams
fdist = nltk.FreqDist(bi_tokens)
fdist.items()[:20]
fdist.plot(50, cumulative=True)

# Freqdist trigrams
fdist2 = nltk.FreqDist(tri_tokens)
fdist2.items()[:20]
fdist2.plot(50, cumulative=True)

# Freqdist fourgrams
fdist4 = nltk.FreqDist(fourgrams)
fdist4.items()[:20]
fdist4.plot(50, cumulative=True)
