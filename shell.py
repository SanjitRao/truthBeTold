from nltk.tokenize import sent_tokenize, word_tokenize
import urllib.request
import re
import json
import newspaper # https://pypi.org/project/newspaper3k/
from nltk.corpus import wordnet
import nltk.tokenize.punkt
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('stopwords')
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

# Takes untokenized text and lemmatizes it
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)
# print([wordnet_lemmatizer.lemmatize(w, get_wordnet_pos(w)) for w in (nltk.word_tokenize(text))])


# Need to replace sentences with text_list and something in the database

url_sentence = "I was wearing a green jacket and blue boots".split()
database_sentence = "I was wearing a red coat and blue shoes".split()

# url_sentence = "The sky is red".split()
# database_sentence = "The sky is blue".split()

stop_words = set(stopwords.words('english'))
stop_words.add("the")

filtered_url_sentence = []
filtered_database_sentence = []


for w in url_sentence:
    if w.lower() not in stop_words:
        filtered_url_sentence.append(w)
for w2 in database_sentence:
    if w2.lower() not in stop_words:
        filtered_database_sentence.append(w2)

print(filtered_url_sentence, filtered_database_sentence)

similarity_list = []

warnings = []

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
