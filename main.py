import schedule
import time
import threading
import requests
import json
import os
from apipoll import Checker
from get_url import GetURL
# Requires: pip install schedule selenium

def start_checker(urls, wait_time):
    checker = Checker(urls, wait_time)

def start_get_url(urls, wait_time):
    get_url = GetURL(urls, wait_time)(urls, wait_time)

urls = os.environ['api_url']
wait_time_api = 15
wait_time_url = 30
threadapi = threading.Thread(target=start_checker, args=(urls, wait_time_api))
threadurl = threading.Thread(target=start_get_url, args=(urls, wait_time_url))
threadapi.start()
threadurl.start()

def runplaylive():
    livefile = open("isLive.txt",'r')
    isLive = livefile.read()
    livefile.close()
    startfile = open("isPlaying.txt",'r')
    started = startfile.read()
    startfile.close()
    current_time = time.strftime("%H:%M:%S", time.localtime())
    if ((isLive == True) and (started == False)):
        print(current_time, "Starting New Live")
        exec(open("playlive.py").read())

    else:
        print(current_time, "Checking Again")
        time.sleep(10)

schedule.every(1).minutes.do(runplaylive)

while True:
    schedule.run_pending()
    time.sleep(1)
