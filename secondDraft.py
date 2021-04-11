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
from nltk.sem import Expression
# read_expr = Expression.fromString
import urllib.request
import re
import json
import newspaper # https://pypi.org/project/newspaper3k/
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
import matplotlib.pyplot as plt
wordnet_lemmatizer = WordNetLemmatizer()



#### INFERENCE DATABASE  ###
inference_test_list = ['Socrates is a man', 'All men are mortal']
p1 = read_expr('man(socrates)')
p2 = read_expr('all x.(man(x) -> mortal(x))')
c  = read_expr('mortal(socrates)')
Prover9().prove(c, [p1,p2]) #Uses Prover9 to logically infer that Socrates is mortal
## TODO: Need a way to convert Strings into Expressions


## TODO: make a copy of database_list, make each item an expression, set up Prover9 and equiv()


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
print(text)## ALLL of our text is here

##PREPROCESSING
text_list = sent_tokenize(text)##Sentence tokenizer

print(text_list)
l = int(len(text_list)) ##Length of textlist
lo = int(len(database_list)) ##Length of database list
print("\n")


d = 0

while d < lo:##as long as d < the length of the database (going through each thing in the database)
    b = 0
    while b < l:##while b < the length of the textlist(going through each sentence)


        print(d)
        X = str(text_list[b]) ##the particular sentence from the text
        Y = str(database_list[d]) ## the particular sentence from the database
        X_list = word_tokenize(X)## word tokenizing
        Y_list = word_tokenize(Y)
        sw = stopwords.words('english')
        l1 =[];l2 =[]
        X_set = {w for w in X_list if not w in sw} ## removing stop words
        Y_set = {w for w in Y_list if not w in sw}
        rvector = X_set.union(Y_set) ## not sure what this is doing

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
    tag = nltk.pos_tag([word])[0][1][0].upper() ##POS Tagging
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)



# meaning of pos abbreviations: https://www.geeksforgeeks.org/part-speech-tagging-stop-words-using-nltk-python/

# tagged = nltk.pos_tag(url_sentence)

# for tag in tagged:
#     print(tag[0], "=", nltk.help.upenn_tagset(tag[1]))

# print(tagged)
# nltk.help.upenn_tagset('RB')





stop_words = set(stopwords.words('english'))
stop_words.add("the")

def get_similarity(url_sentence, database_sentence):
    url_sentence = url_sentence.split()
    database_sentence = database_sentence.split()

    filtered_url_sentence = []
    filtered_database_sentence = []


    for w in url_sentence:
        if w.lower() not in stop_words:
            filtered_url_sentence.append(w)
    for w2 in database_sentence:
        if w2.lower() not in stop_words:
            filtered_database_sentence.append(w2)#**Database should already be guuci

    print(filtered_url_sentence, filtered_database_sentence)

    similarity_list = []

    warnings = []

    for i in range(len(filtered_url_sentence)):
        word1 = wordnet.synset(wordnet_lemmatizer.lemmatize(filtered_url_sentence[i], get_wordnet_pos(filtered_url_sentence[i])) + "." + get_wordnet_pos(filtered_url_sentence[i]) + ".01")
        word2 = wordnet.synset(wordnet_lemmatizer.lemmatize(filtered_database_sentence[i], get_wordnet_pos(filtered_database_sentence[i])) + "." + get_wordnet_pos(filtered_database_sentence[i]) + ".01")
        print(filtered_url_sentence[i], "and", filtered_database_sentence[i], ":", word1.wup_similarity(word2))
        if word1.wup_similarity(word2) == None:
            similarity_list.append(-1)#TODO -1 or 0?
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
    elif (final_similarity >= 0.85):
        print("Lez go")

    else:
        for warning in warnings:
            print("Warning:", warning, "do not match.")

    return final_similarity

url_sentences = "I was wearing a green jacket and blue boots"
database_sentences = "I was wearing a red coat and blue shoes"
get_similarity(url_sentences, database_sentences)

database_list = ['Hello.', "This is a test website that doesn't do anything cool.", 'bla.', "This test website is pretty useless"]
url_sentence = "The sky is red".split()
database_sentence = "The sky is blue".split()

# weird cases:
# quick and fast have a similarity of 0.11764705882352941
# novel and book have a similarity of 0.1111111111111111
# inside and outside have a similarity of 0.8333333333333334

true_sentences = ["I was wearing a red jacket and blue boots", "The athlete is quick", "The textbook is on the bookshelf", "The little boat is in the sea"]
false_sentences = ["I was wearing a green jacket and blue boots", "The runner is slow", "The book is on the table", "The gigantic ship is on the land"]
temp_database = ["I was wearing a red coat and blue shoes", "The swimmer is fast", "The book is on the shelf", "The small ship is in the ocean"]

true_values = []
false_values = []

for index in range(len(temp_database)):
    true_values.append(get_similarity(true_sentences[index], temp_database[index]))
    false_values.append(get_similarity(false_sentences[index], temp_database[index]))

print("\n\n\n")
print("True Values:", true_values)
print("False Values:", false_values)

plt.scatter(true_values, [1]*len(true_values), label= "stars", color= "green", marker= "*", s=20)
plt.scatter(false_values, [0]*len(false_values), label= "stars", color= "red", marker= "*", s=20)

plt.xlim(-0.25, 1.25)
plt.ylim(-0.5, 1.5)

plt.show()
