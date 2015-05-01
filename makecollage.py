# -*- coding: utf-8 -*-
"""
Created on Fri May 01 16:29:25 2015

@author: Stephen Bishop
"""

# import the library from my site-packages folder:
# C:\Users\Stephen Bishop\Anaconda\Lib\site-packages\collage
from collage import preprocess as make

# open the text file of the speech we'll be using
storytext = open("DrumMajor.txt").read()

# run this line of code to spit out everything we need
make.collage(storytext)