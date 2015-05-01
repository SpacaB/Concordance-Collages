# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 20:31:43 2015

@author: Stephen Bishop
"""

import re
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from nltk import FreqDist

storytextIKE = open("goodbyeike.txt").read()

# Function to preprocess words into tokens
def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	return " ".join(tokens)


preprocessedStory = preprocess(storytextIKE)
tokens = nltk.word_tokenize(preprocessedStory)
print tokens[0:20]
len(tokens)


stop = stopwords.words('english')
remstopIKE = [i for i in tokens if i not in stop]
remstopIKE[0:20]
len(remstopIKE)

# 1684 tokens --> 828 without stopwords
fdist2 = FreqDist(remstopIKE)
print(fdist2)
fdist2.most_common()[:20]
fdist2.plot(50, cumulative=True)


# Turn it into an nltk text object
SpeechText = nltk.Text(tokens)
SpeechText.concordance('must', lines=38)
SpeechText.concordance('balance', lines=38)
SpeechText.concordance('military', lines=38)
SpeechText.concordance('peace', lines=38)
SpeechText.concordance('every', lines=38)
SpeechText.concordance('nation', lines=38)
SpeechText.concordance('world', lines=38)
SpeechText.concordance('government', lines=38)
SpeechText.concordance('war', lines=38)