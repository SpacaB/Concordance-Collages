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

storytextDrum = open("DrumMajor.txt").read()

# Function to preprocess words into tokens
def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	return " ".join(tokens)


preprocessedStory = preprocess(storytextDrum)
tokens = nltk.word_tokenize(preprocessedStory)
print tokens[0:20]
len(tokens)


stop = stopwords.words('english')
remstopDrum = [i for i in tokens if i not in stop]
remstopDrum[0:20]
len(remstopDrum)

# 5150 tokens --> 2293 without stopwords
fdist2 = FreqDist(remstopDrum)
print(fdist2)
fdist2.most_common()[:20]
fdist2.plot(50, cumulative=True)


# Turn it into an nltk text object
SpeechText = nltk.Text(tokens)
SpeechText.concordance('know', lines=38)
SpeechText.concordance('major', lines=38)
SpeechText.concordance('yes', lines=38)
SpeechText.concordance('people', lines=38)
SpeechText.concordance('say', lines=38)


