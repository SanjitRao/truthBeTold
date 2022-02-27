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


from urllib.request import urlopen
from bs4 import BeautifulSoup
url = 'ASSUME WE HAVE THE LINK ALREADY'
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)

def sentence_tokenizer():
    article_sentence_tokens = sent_tokenize(text, language="english") #list of sentences now
    return article_sentence_tokens



























