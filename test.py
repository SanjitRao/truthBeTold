'''
Plan:
Retrieve URL
Parse for paragraphs/other meaningful text
//Covered using urllib module

“Read”; builds a KB and uses previous knowledge, makes inferences and determines degree of validity using probability; NLP

Spits out answer (Graph, %’s , tables, etc)

Storage (How will this data be used?)
     - Add to KB
     - Make inferences about other topics (if possible)


'''
import urllib.request
import urllib.parse
from urllib.parse import urlparse
import re
import wsgiref.simple_server

print("Enter a URL")
url = input()
try:
    headers = {}

















    headers['User Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    req = urllib.request.Request(url, headers = headers)
    #print(req)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    #print(respData)

    paragraphs = re.findall(r'<p> (.*?) </p>', str(respData))
    print(paragraphs)
    for eachP in paragraphs:
        print(eachP)

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()


except Exception as e:
    print(str(e))