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

storytextFDR = open("FDRinaug.txt").read()

# Function to preprocess words into tokens
def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	return " ".join(tokens)


preprocessedStory = preprocess(storytextFDR)
tokens = nltk.word_tokenize(preprocessedStory)
print tokens[0:20]
len(tokens)


stop = stopwords.words('english')
remstopFDR = [i for i in tokens if i not in stop]
remstopFDR[0:20]
len(remstopFDR)

# 1684 tokens --> 828 without stopwords
fdist2 = FreqDist(remstopFDR)
print(fdist2)
fdist2.most_common()[:20]
fdist2.plot(50, cumulative=True)


# Turn it into an nltk text object
SpeechText = nltk.Text(tokens)
SpeechText.concordance('must', lines=38)
SpeechText.concordance('national', lines=38)
SpeechText.concordance('people', lines=38)
SpeechText.concordance('may', lines=38)
SpeechText.concordance('action', lines=38)
SpeechText.concordance('shall', lines=38)
SpeechText.concordance('helped', lines=38)
SpeechText.concordance('leadership', lines=38)
SpeechText.concordance('world', lines=38)