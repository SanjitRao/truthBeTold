from newsapi import NewsApiClient
from bs4 import BeautifulSoup
import lxml
import requests
import datetime as dt
import pandas as pd
#TBT's NewsAPI key: ee08accb3d36479789b2659c9da1a59d (need to imput as a string)

#TODO: 1) fill news_orgs_dict with ~20 news orgs.
#      2) create a try-exception catch in case the totalResults == 0
#      3) this function might be computationally expensive... is there a more efficient way?
news_orgs_dict = {'bbc-news': [['meta content', 'asasdsdasd'], ['p', 'ssrcss-1q0x1qg-Paragraph eq5iqo00']]}
def keyword_newsSource_searchAlg(keyword, news_source, news_orgs_dict=news_orgs_dict, API_KEY = 'ee08accb3d36479789b2659c9da1a59d'): # (Str, Str, Str)
    newsapi= NewsApiClient(API_KEY)
    data = newsapi.get_everything(q=keyword, sources=news_source, language='en')
    text_tags = news_orgs_dict[news_source] # 'tags' should now be a list of all the text-containing tags for that particular news source
    rv = [] # 'return value'
    for num_article in range(data['totalResults']+1): # +1 just in case there aren't any results; gotta create a catch-exception for that
        source_HTML = requests.get(data['articles'][num_article]['url']).text
        soup = BeautifulSoup(source_HTML, 'lxml')
        text_html = ''
        for pair in text_tags:
            text_html+= str(soup.find_all(pair[0], class_=pair[1]))
        rv.append(text_html)
    return rv
# to import this function into other TBT_Algorithms files: from NewsAPI import keyword_newsSource_searchAlg