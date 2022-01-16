from truthBeTold.TBT_Data.false import *
from truthBeTold.TBT_Data.true import *

from nltk.sentiment.vader import SentimentIntensityAnalyzer


def polarization_analyser(article_text):  # polarization analyzer
    polarscore = SentimentIntensityAnalyzer().polarity_scores(article_text)
    if (polarscore['neg'] > polarscore['pos']):
        return -1 * polarscore['neg']
    elif (polarscore['neg'] < polarscore['pos']):
        return polarscore['pos']
    else:
        return 0


from textblob import TextBlob


def sub_or_Obj(data):  # output is a decimal
    rv = TextBlob(data)
    return rv.sentiment.subjectivity


import csv

for i in text_true:
    cool_list = []
    cool_list.append(polarization_analyser(i))
    cool_list.append(sub_or_Obj(i))
    cool_list.append("1") # 1 represents fact
    with open('../TBT_Data/data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(cool_list)

for i in text_false:
    cool_list = []
    cool_list.append(polarization_analyser(i))
    cool_list.append(sub_or_Obj(i))
    cool_list.append("0") # 0 represents false info
    with open('../TBT_Data/data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(cool_list)