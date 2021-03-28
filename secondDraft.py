import spacy
import nltk
import numpy
import selenium
from bs4 import BeautifulSoup
import lxml
import requests
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import urllib.request
import re
import json
import newspaper # https://pypi.org/project/newspaper3k/
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

database_list = ['Hello.', "This is a test website that doesn't do anything cool.", 'bla.', "This test website is pretty useless"]

url = 'file:///Users/Siddharth/Desktop/Desktop/website.html'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()
paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))
lis = []
for eachP in paragraphs:
    lis.append(eachP)
text = " "
text = text.join(lis)
print(text)


text_list = sent_tokenize(text)

print(text_list)
l = int(len(text_list))
lo = int(len(database_list))
print("\n")


d = 0

while d < lo:
    b = 0
    while b < l:


        print(d)
        X = str(text_list[b])
        Y = str(database_list[d])
        X_list = word_tokenize(X)
        Y_list = word_tokenize(Y)
        sw = stopwords.words('english')
        l1 =[];l2 =[]
        X_set = {w for w in X_list if not w in sw}
        Y_set = {w for w in Y_list if not w in sw}
        rvector = X_set.union(Y_set)

        for w in rvector:
            if w in X_set: l1.append(1)
            else: l1.append(0)
            if w in Y_set: l2.append(1)
            else: l2.append(0)
        c = 0


        for i in range(len(rvector)):
                c+= l1[i]*l2[i]
        cosine = c / float((sum(l1)*sum(l2))**0.5)
        print("similarity: ", cosine)

        b+=1
    d+=1



print("\n")
matched_list = []


# nltk syntatic entailment

# nltk.COOLFUnction("text")

# Tensorflow has cool ml stuff

# https://wordnet.princeton.edu/

# word2vec
b = 0

for i in text_list:
    if str(i) in database_list:
        print("Match: ", i)
        matched_list.append(i)
        b += 1
    else:
        print("No match")
        b += 1



# add if statements to segregate by topic.

with open('dataset.json','w') as outfile:
    json.dump(matched_list,outfile)


# ---------------------------------------------------------------------------
# Need to replace sentences with text_list and something in the database

def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)

url_sentence = "I was wearing a green jacket and blue boots".split() # replace with sentence from the article
database_sentence = "I was wearing a red coat and blue shoes".split() # replace with fact from database

# url_sentence = "The sky is red".split()
# database_sentence = "The sky is blue".split()

stop_words = set(stopwords.words('english'))
stop_words.add("the")

filtered_url_sentence = []
filtered_database_sentence = []

# remove stop words
for w in url_sentence:
    if w.lower() not in stop_words:
        filtered_url_sentence.append(w)
for w2 in database_sentence:
    if w2.lower() not in stop_words:
        filtered_database_sentence.append(w2)

print(filtered_url_sentence, filtered_database_sentence)

similarity_list = []

warnings = []

# find similarity

for i in range(len(filtered_url_sentence)):
    word1 = wordnet.synset(wordnet_lemmatizer.lemmatize(filtered_url_sentence[i], get_wordnet_pos(filtered_url_sentence[i])) + "." + get_wordnet_pos(filtered_url_sentence[i]) + ".01")
    word2 = wordnet.synset(wordnet_lemmatizer.lemmatize(filtered_database_sentence[i], get_wordnet_pos(filtered_database_sentence[i])) + "." + get_wordnet_pos(filtered_database_sentence[i]) + ".01")
    print(filtered_url_sentence[i], "and", filtered_database_sentence[i], ":", word1.wup_similarity(word2))
    if word1.wup_similarity(word2) == None:
        similarity_list.append(0)
        warnings.append([filtered_url_sentence[i], filtered_database_sentence[i]])
    else:
        similarity_list.append(word1.wup_similarity(word2))

similarity_total = 0
for n in similarity_list:
    similarity_total += n

final_similarity = similarity_total/len(similarity_list)

print("Final Similarity:", final_similarity)
if len(warnings) == 0:
    print("Warnings: None")
else:
    for warning in warnings:
        print("Warning:", warning, "do not match.")
