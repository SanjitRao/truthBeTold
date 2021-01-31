##ALL IMPORTED MODULES AND LIBRARIES



'''
##EXTRACTING TEXT FROM HTML AND PREPROCESSING THE DATA



##ASSESSING VALIDITY



##OUTPUTING THE TBT SCORE
















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