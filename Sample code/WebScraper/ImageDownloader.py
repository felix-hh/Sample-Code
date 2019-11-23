import requests, bs4, webbrowser,pprint
print ("enter the search term to download images: ")
search = input()
def downloadSearch(search):
    path = ".\\descargas\\"+search+"_searchImages.html"
    res = open(path, "wb")
    res.write(requests.get("https://www.bing.com/images/search?q=" + search).content)
    res.close()
    return path

def getSoup(search):
    with open(downloadSearch(search),"rb") as f:
        soup = bs4.BeautifulSoup(f.read(),features="html.parser")
    return soup

searchSoup = getSoup(search)
images = searchSoup.select(".thumb")
for image in images:
    try:
        with open(".\\descargas\\"+image.get("href").split("/")[-1], "wb") as f:
            res = requests.get(image.get("href"))
            for chunk in res.iter_content(100000):
                f.write(chunk)
        print("Downloaded")
    except Exception as err:
        print(err)
    print (images.index(image))
