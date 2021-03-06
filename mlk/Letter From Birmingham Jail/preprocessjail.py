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

storytextDream = open("jailletter.txt").read()

# Function to preprocess words into tokens
def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	return " ".join(tokens)


preprocessedStory = preprocess(storytextDream)
tokens = nltk.word_tokenize(preprocessedStory)
print tokens[0:20]
len(tokens)


stop = stopwords.words('english')
remstopDream = [i for i in tokens if i not in stop]
remstopDream[0:20]
len(remstopDream)

# 6943 tokens --> 3455 without stopwords
fdist2 = FreqDist(remstopDream)
print(fdist2)
fdist2.most_common()[:20]
fdist2.plot(50, cumulative=True)


# Turn it into an nltk text object
SpeechText = nltk.Text(tokens)
SpeechText.concordance('would', lines=38)
SpeechText.concordance('law', lines=38)
SpeechText.concordance('negro', lines=38)
SpeechText.concordance('must', lines=38)
SpeechText.concordance('church', lines=38)
SpeechText.concordance('birmingham', lines=38)
SpeechText.concordance('time', lines=38)
SpeechText.concordance('white', lines=38)