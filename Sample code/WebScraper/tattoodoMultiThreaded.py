###Image Webscraper that scrolls to the end of the page and obtains image sources to download. Multithreaded version to optimize bandwith consumption
###Checks with previous data how many images had been already downloaded. Updates this list. If specified an existing folder, downloads only nonexisting.

### Importing modules

import time,requests,tqdm,copy,os,threading,re,winsound, random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

### Defining functions

#Obtains source links of loaded images and appends if non-repeated and valid according to some settings.
##It should also store the url's of the filtered images for future program updates.
def scan():
    global imagesUrl
    global discardedUrl
    ###################
    global previousCount
    global previousImagesList
    ###################
    images = browser.find_elements_by_tag_name("img")
    foundSomething = False
    for image in images:
        try:
            url = image.get_attribute("src")
            if url not in imagesUrl:
                if url.startswith("http") and not url.endswith("20"):
                    imagesUrl.append(url)
                ###################################
                if url in previousImagesList:
                    previousCount +=1
                ###################################
                else:
                    discardedUrl.append(url)
        except:
            pass

#Scrolls down the page
def advance():
    browser.execute_script("window.scrollTo(0, "+str(scrollPos)+")")

#Downloads image from source, names according to counter. If image not downloaded, stores counter and source to retry in errors.txt. 
def download(url,counter,path):
    try:
        with open(path+os.path.sep+"image"+str(counter)+".jpg","wb") as f:
            f.write(requests.get(url).content)
    except:
        with open(path+os.path.sep+"errors.txt","a") as f:
            f.write(str(counter)+": "+url+"\n")

### Obtaining the parameters

searchRegex = re.compile(".*\?.*?=([A-Za-z_]*).*")
print ("Enter the name of the page to scan including https://")
web = input()
possibleFolderName = searchRegex.search(web)[1]
print ("Enter the name of the directory to download in C:\\python37\\descargas\\ or skip to assign C:\\python37\\descargas\\"+possibleFolderName)
dirName = input()
if not dirName:
    dirName = possibleFolderName
newDirPath = "\\python37\\descargas\\"+dirName

### Loading webpage and making settings
browser = webdriver.Firefox()
browser.get(web)
imagesUrl = []
discardedUrl =[]
downloadThreadList = []
scrollPos=0
time.sleep(3)

############################
previousImagesList=open("\\python37\\descargas\\geometric2\\downloaded.txt","r").readlines()
for i in range(len(previousImagesList)):
    previousImagesList[i] = previousImagesList[i][:-1]
previousCount = 0
############################

###Core of the program
startTime=time.time()
while True:
    scrollPos+=500
    scan()
    advance()
    #time.sleep(0.1)
    if scrollPos>browser.execute_script("return document.documentElement.scrollHeight"):
        print ("end of page at pos "+str(scrollPos)+" and time " + str(round(time.time()-startTime))+" sec. Total images found: "+str(len(imagesUrl)))
        ################################################
        print ("%d images had already been downloaded" %previousCount)
        ################################################
        break
winsound.Beep(1000,2000) ### download starts beep
counter = 0
os.mkdir(newDirPath) 
with open(newDirPath+os.path.sep+"discarded.txt","w") as f:
    f.write("Discarded sources:\n")
    for url in discardedUrl:
        f.write(url+"\n")
with open(newDirPath+os.path.sep+"downloaded.txt","w") as f:
    for url in imagesUrl:
        f.write(url+"\n")
with open(newDirPath+os.path.sep+"errors.txt","w") as f:
    f.write("Failed to download:\n")



for url in tqdm.tqdm(imagesUrl):
    threadObj = threading.Thread(target=download, args=[url,counter,newDirPath])
    downloadThreadList.append(threadObj)
    threadObj.start()
    counter +=1

for thread in downloadThreadList:
    thread.join()
print("Downloads completed")
with open(newDirPath+os.path.sep+'errors.txt','r') as f:
    errorsString= f.read()
    print(errorsString)
    if errorsString == "Failed to download:\n":
        noErrors = True
if noErrors:
    os.remove(newDirPath+os.path.sep+'errors.txt')

winsound.Beep(1000,2000) ###Finish Beep

