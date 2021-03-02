from nltk.tokenize import sent_tokenize, word_tokenize
import urllib.request
import re
import json
import newspaper # https://pypi.org/project/newspaper3k/
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