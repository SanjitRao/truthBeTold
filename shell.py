from nltk.tokenize import sent_tokenize, word_tokenize
import urllib.request
import re
import json
import newspaper # https://pypi.org/project/newspaper3k/
from nltk.corpus import wordnet
import nltk.tokenize.punkt
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')
wordnet_lemmatizer = WordNetLemmatizer()
nltk.download('averaged_perceptron_tagger')

database_list = ['Hello.', "This is a test website that doesn't do anything cool.", 'bla.']


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
print("\n")

# Takes untokenized text and lemmatizes it
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)
print([wordnet_lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in (nltk.word_tokenize(text))])

matched_list = []

# implement ml:
for i in text_list:
    if str(i) in database_list:
        print("Match: ", i)
        matched_list.append(i)
    else:
        print("No match")

# add if statements to segregate by topic.

with open('dataset.json','w') as outfile:
    json.dump(matched_list,outfile)
