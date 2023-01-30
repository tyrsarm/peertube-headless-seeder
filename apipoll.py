import json
import requests 
import time
import os

class Checker:
    def __init__(self, urls, wait_time):
        self.wait_time = wait_time
        self.urls = urls
        self.videos = self.get_videos()
        self.main_loop()
    
    @staticmethod
    def get_data(url):
        set_url = os.environ['api_url']
     #   urlfile = open("api_url.txt",'r')
     #   set_url = urlfile.read()
     #   urlfile.close()
        url_input = requests.get(set_url).json()['data']
        data = json.dumps(url_input)
        data_dict = json.loads(data)
        videos = [videos['id'] for videos in data_dict]
        return videos
    
    def get_videos(self):
        videos = set()
        for url in self.urls:
            videos.update(Checker.get_data(url))
        return videos

    def check_new_videos(self):
        new_videos = self.get_videos()
        
        videos_diff = list(new_videos.difference(self.videos))
        
        current_time = time.strftime("%H:%M:%S", time.localtime())
        
        if len(videos_diff) > 0:
            print(current_time, videos_diff)
            new_id = str(list(new_videos.difference(self.videos)))
            print(new_id)
            with open("new_id.txt",'w') as idfile:
                 pass
            idfile = open("new_id.txt", "w+")
            idfile.write(new_id)
            idfile.close()
        else:
            print(current_time, "No new videos")

        self.videos = new_videos
    
    def main_loop(self):
        while True:
            time.sleep(self.wait_time)
            self.check_new_videos()
