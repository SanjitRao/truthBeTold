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
import re
import wsgiref.simple_server


def application(environ, start_response):
    headers = [('Content-Type', 'text/plain; charset=utf-8')]
    start_response('200 OK', headers)

    s = "environ['PATH_INFO'] = " + environ['PATH_INFO'] + '\n' + \
        "environ['QUERY_STRING'] = " + environ['QUERY_STRING'] + '\n'
    listPath = [];
    for i in range(len(environ["PATH_INFO"])):
        if(environ["PATH_INFO"][i] == "\\"):
            j=0
            listPath[i] = "\\"
            while(environ["PATH_INFO"][i+j+1] != "\\"):
                listPath[i] += environ["PATH_INFO"][i+j+1]
                j+=1


    return [environ["PATH_INFO"][1].encode()]


httpd = wsgiref.simple_server.make_server('', 8000, application)
httpd.serve_forever()

#Take in a url from the user (Won't look like this in the final version)
print("Copy-paste URL here")
url = input()

values =




print("hello world")
v = "tbt"
print(v)
print("something")
print("My change")

v= 5
x = 10
print(x/v)
