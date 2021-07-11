import newspaper
def getTitles_Authors_Text(root_URL):
    channel_cache = newspaper.build(root_URL)
    cca = channel_cache.articles
    rv = ""
    for i in range(int(len(cca)/9)):
        a = cca[i]
        a.download()
        a.parse()
        rv += "\n" + a.title + str(a.authors) + "\n" + a.text
    print(int(len(cca)/9))
    return rv
rv = getTitles_Authors_Text("https://chicago.suntimes.com/%22")
print(rv)

#actionnews3.com

