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

storytext = open("otheramerica.txt").read()

# Function to preprocess words into tokens
def preprocess(sentence):
	sentence = sentence.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(sentence)
	return " ".join(tokens)


preprocessedStory = preprocess(storytext)
tokens = nltk.word_tokenize(preprocessedStory)
print tokens[0:20]
len(tokens)


stop = stopwords.words('english')
remstop = [i for i in tokens if i not in stop]
remstop[0:20]
len(remstop)

# 5810 tokens --> 2670 without stopwords
fdist2 = FreqDist(remstop)
print(fdist2)
fdist2.most_common()[:20]
fdist2.plot(50, cumulative=True)


# Turn it into an nltk text object
SpeechText = nltk.Text(tokens)
SpeechText.concordance('america', lines=47)
SpeechText.concordance('negro', lines=38)
SpeechText.concordance('nation', lines=38)
SpeechText.concordance('white', lines=38)
SpeechText.concordance('negroes', lines=38)
SpeechText.concordance('struggle', lines=38)
SpeechText.concordance('justice', lines=38)
SpeechText.concordance('problems', lines=38)
SpeechText.concordance('freedom', lines=38)
SpeechText.concordance('rights', lines=38)