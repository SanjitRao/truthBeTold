#!pip install newsapi-python
#!pip install beautifulsoup4
#!pip install lxml
#!pip install requests

from newsapi import NewsApiClient
from bs4 import BeautifulSoup
from urllib.request import urlopen
import lxml
import requests
import datetime as dt
import pandas as pd

import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
nltk.download('wordnet')      #download if using this module for the first time


from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')    #download if using this module for the first time


#For Gensim
import gensim
import string
from gensim import corpora
from gensim.corpora.dictionary import Dictionary
from nltk.tokenize import word_tokenize
#TBT's NewsAPI key: ee08accb3d36479789b2659c9da1a59d (need to imput as a string)

#TODO: 1) fill news_orgs_dict with ~20 news orgs.
#      2) create a try-exception catch in case the totalResults == 0
#      3) this function might be computationally expensive... is there a more efficient way?

api_key = 'ee08accb3d36479789b2659c9da1a59d'

def keyword_NS_searchAlg_V2(keyword, news_source, API_KEY = api_key): # (Str, Str, Str)
  newsapi= NewsApiClient(API_KEY)
  data = newsapi.get_everything(q=keyword, sources=news_source, language='en')
  rv = []
  for article_num in range(len(data['articles'])):
    url = str(data['articles'][article_num]['url'])
  #"http://news.bbc.co.uk/2/hi/health/2284783.stm"
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
    rv.append(text)
  return rv

#Test
bbc_bitcoin_text = keyword_NS_searchAlg_V2('bitcoin', 'bbc-news')
for text in bbc_bitcoin_text:
  print(text)
  print()



def BoW_Topic_Identification():
  ref_texts = keyword, news_source, API_KEY = api_key