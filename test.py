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
from urllib.parse import urlparse
import re
import wsgiref.simple_server


#parse = urlparse(inputUrl)
#print(parse) #[2] gives path, [1] gives main site, [4] gives Query String
#ParseResult(scheme='https', netloc='www.youtube.com', path='/watch', params='',
#            query='v=GEshegZzt3M&t=282s', fragment='')
#Take in a url from the user (Won't look like this in the final version)


'''values = {}
for i in range(len(parse[4])-1): #len(query string)
    #if "=", then values[parse[4][i-1]] += "coiiofdi943" while
    if parse[4][i:i+2] == (parse[4][i] + "="):
        values[parse[4][i]] = ""
        j = 1
        while (i+j+1 < len(parse[4])) and (parse[4][i+j+1] != "&"):
            values[parse[4][i]] +=  parse[4][i+j+1]
            j+=1
        #optimization: set i = j+2
print(values)'''
'''url = "https://www." + parse[1]#different then the prev. url; main site + path
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()'''

#print(respData)
##print(url)

print("Enter a URL")
url = input()
try:

    headers = {}
    headers['User Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    req = urllib.request.Request(url, headers = headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    paragraphs = re.findall(r'<p> (.*?) </p>', str(respData))
    for eachP in paragraphs:
        print(eachP)

    saveFile = open('withHeaders.txt', 'w')
    saveFile.write(str(respData))
    saveFile.close()


except Exception as e:
    print(str(e))