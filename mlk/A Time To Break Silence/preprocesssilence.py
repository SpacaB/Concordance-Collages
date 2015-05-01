# -*- coding: utf-8 -*-
"""
Created on Sat Feb 14 20:31:43 2015

@author: Stephen Bishop
"""

import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
from nltk import FreqDist

storytext = open("timetobreaksilence.txt").read()

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


from nltk.corpus import stopwords
stop = stopwords.words('english')
remstop = [i for i in tokens if i not in stop]
remstop[0:20]
len(remstop)

# 6779 tokens --> 3295 without stopwords
fdist2 = FreqDist(remstop)
print(fdist2)
fdist2.most_common()[:20]
fdist2.plot(50, cumulative=True)


# Turn it into an nltk text object
SpeechText = nltk.Text(tokens)
SpeechText.concordance('vietnam', lines=38)
SpeechText.concordance('war', lines=38)
SpeechText.concordance('government', lines=38)
SpeechText.concordance('revolution', lines=38)
SpeechText.concordance('nation', lines=38)

