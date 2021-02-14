##ALL IMPORTED MODULES AND LIBRARIES
import nltk

##EXTRACTING TEXT FROM HTML AND PREPROCESSING THE DATA
htmlTESTString = '''
<!DOCTYPE html>
<html>
<body>           
<h1> TBT Very Simple HTML </h1>

<p> Humans breathe oxygen. Cats can fly. The sky is blue. </p>

 Humans = breathe(oxygen)

</body>
</html>
'''

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