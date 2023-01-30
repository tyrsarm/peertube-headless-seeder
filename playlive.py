from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time

def startFF():
    urlfile = open("url_file.txt",'r')
    url = urlfile.read()
    urlfile.close()
    options = FirefoxOptions()
    options.add_argument("--headless")
    options.set_preference('media.autoplay.default', 0)
    driver = webdriver.Firefox(options=options)
    driver.get(url)

livefile = open("isLive.txt",'r')
isLive = livefile.read()
livefile.close()
startfile = open("isPlaying.txt",'r')
started = startfile.read()
startfile.close()
print(f"Main Running")
if ((isLive == True) and (started == False)):
    startFF()
    with open("isPlaying.txt",'w') as playingfile:
        pass
    playingfile.close()
    playingfile = open("isPlaying.txt.txt", "w+")
    playingfile.write("True")
    playingfile.close()
    while isLive == True:
        time.sleep(630)
        livefile = open("isLive.txt",'r')
        isLive = livefile.read()
        livefile.close()
    with open("isPlaying.txt",'w') as playingfile:
        pass
    playingfile.close()
    playingfile = open("isPlaying.txt.txt", "w+")
    playingfile.write("False")
    playingfile.close()    
    driver.close()
    exit()
else:
    exit()

