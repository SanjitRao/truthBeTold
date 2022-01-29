##ALL IMPORTED MODULES AND LIBRARIES
import requests
import bs4 as BeautifulSoup
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize #download is not working for me for some reason
#from nltk.corpus import stopwords, from nltk.tokenize import PunktSentenceTokenizer, from nltk.corpus import wordnet, from nltk.stem import WordNetLemmatizer
#nltk.download('averaged_perceptron_tagger'), nltk syntatic entailment, word2vec
import stanfordnlp as snlp
en = snlp.Pipeline(lang='en', processors='tokenize') #change to 'pos' for POS tagging or 'depparse' for dependency parsing
import pandas as pd
import spacy
import numpy
#import newspaper # https://pypi.org/project/newspaper3k/
import matplotlib.pyplot as plt

#(DELETE THIS LATER): This python file is meant to collect, extract the raw text if needed, and preprocess the text as needed.
# It may be prudent to check if the stopwords, punctuation, #capital letters, etc. give any indication of misinformation.
# The goal of this file should be to see 1) what kind of preprocessing & vectorization is actually needed and 2) create a
# feature function that takes into account the stop words, lemmas, etc (whatever we decide on, if that makes sense)
# - don't do cosine similarity. Skip right to Word2Vec (or TF-IDF at the very LEAST)
# - see how Beautiful soup, dfs, newspaper, etc could be used to build a framework for gathering text from an article(s)
    #- this will likely be a long process, so create a good structure to set in motion

link = ''
HTML = requests.get(link)


























