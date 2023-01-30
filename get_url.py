import json
import requests
import time


class GetURL:
  def __init__(self, urls, wait_time):
      self.wait_time = wait_time
      self.urls = urls
      self.main_loop()
      self.GetData()
 # This function takes an id as an input then will return back the url for that id
  def checkURL(self, id):
     r = requests.get(self.urls).json()['data']
     data = json.dumps(r)
     data_dict = json.loads(data)
     for items in data_dict:
        if id == items['id']:
            with open("url_file.txt", 'w') as urlfile:
                pass
            urlfile = open("url_file.txt", "w+")
            urlfile.write(items['url'])
            urlfile.close()
            return items['url']
     return 'id not found'
 # This function takes an id as an input then will return back the isLive value for that id
  def checkLive(self, id):
      num = 0
      r = requests.get(self.urls).json()['data']
      data = json.dumps(r)
      data_dict = json.loads(data)
      for items in data_dict:
        if id == items['id']:
          with open("isLive.txt",'w') as livefile:
            pass
          livefile = open("isLive.txt", "w+")
          livefile.write(str(items['isLive']))
          livefile.close()
          return items['isLive']
      return 'id not found'
 #  This is the loop funtion to update the ID and run the two functions above
  def main_loop(self):
    while True:
      time.sleep(self.wait_time)
      idfile = open("new_id.txt",'r')
      newid = int(idfile.read())
      idfile.close()
      print(f"Data Loaded")
      self.checkURL(newid)
      print(f"Got URL")
      self.checkLive(newid)
