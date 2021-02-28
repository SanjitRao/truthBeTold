##ALL IMPORTED MODULES AND LIBRARIES
import urllib.request
import urllib.parse
import re
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize #download is not working for me for some reason
from nltk.tokenize import PunktSentenceTokenizer

htmlTESTString = '''
<!DOCTYPE html>
<html>
<body>           
<h1> TBT Very Simple HTML </h1>

<p> Humans breathe oxygen. Cats can fly. The sky is blue. </p>


</body>
</html>
'''
##EXTRACTING TEXT FROM HTML AND PREPROCESSING THE DATA
url = "Base url"
values = {'variable': "value"}

data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<p>(.*?)</p>', str(respData))
#paragraphs = "Humans breathe oxygen. Cats can fly. The sky is blue."
##***This code requires we hardcode a url and its query string***

'''nltk to extract parts of speech
- https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/
-NLTK
    - subject = ?  action = ? object = ? verb = ? 
    - tense = ? "Trump was president vs trump is president" ***Assume present tense
    - remove stop words
    - Lemmatization (think abt tense)
    - Normalization

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
words = word_tokenize(paragraphs)
stop_words = set(stopwords.words("english"))
filtered_words = [w for w in words if not in stop_words]
    #Maybe not use it?
'''
#Preprocessing
tokenizedText = sent_tokenize(paragraphs)
#['Humans breath oxygen.', 'Cats can fly.'. The sky is blue.']

train_text = '''This is text to pretrain PunktSentenceTokenizer. I know that cats are great! Humans need oxygen to survive.
               Cats do not have the ability to fly, and the sky is blue.'''
sample_text = paragraphs
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():#will store each word allong with their part of speech in 'tagged'
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
    except Exception as e:
        print(e)
















'''
DATABASE
- how to create ==> JSON?
- Segregate into different topcis and subjects
    - Date
    - https://datatofish.com/create-database-python-using-sqlite3/ <== trying to create a database
        - segregated by country, date, and client
        - we could segregate by date and validity?
'''
'''
**import urllib.request
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
print(html)**

After extraction
- Tokenize using nltk and/or textblob
-Normalization: convert everything to same thing (lowercase, tense??? 
- need DATE of data**<== allow us to determine if data is dated
- https://www.webnots.com/how-to-find-last-updated-date-of-a-web-page/ <== check date!


Textblob - textblob function => tokenization and spelling correction
CoreNLP - part of teach tagging, 
nltk to do part of speech tagging

Selenium - automated html extraction
Regex - extracting  
from urllib.request import urlopen

**from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)**

nltk can identify subjects and verbs (to put into Subject = Action(Object))
- can use variables to represent parts of speech

'''

##ASSESSING VALIDITY
'''
Form: 
subject defined by action and object
- Subject = Action(Object)
    - Above form needs to be compatible with databases
- Link pronouns to the name ("He" == "John")
    


- ***find websites that we can use as a credible benchmark for new information
   - Check date!
   - Make sure its not an opinion piece (nltk)***
   
CoreNLP - part of teach tagging, Full neural network pipeline for robust text analytics, including tokenization, multi-word token (MWT) expansion, lemmatization, 
part-of-speech (POS) and morphological features tagging, dependency parsing, and named entity recognition;   

Pattern 
Gensim 
 
'''


## OUTPUTING THE TBT SCORE
'''
Highlight innacurate phrases
- Selenium: basically inspect element capabilities  

'''

#Data extraction




#Now is list of sentences



