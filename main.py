import time

import requests
from threading import Thread
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver


def get_live_video_urls(instance_url="https://jupiter.tube/"):
    """
    Get a list of URLs for the videos that are currently live.
    :param instance_url: base url of the PeerTube instance that will be called
    :return: list of URLs as strings
    """
    search_url: str = f"{instance_url}api/v1/search/videos?isLive=false&sort=-publishedAt"
    videos_json = requests.get(search_url).json()
    return [v["url"] for v in videos_json["data"]]


def run_browser_instance(url: str = None) -> WebDriver:
    """
    Create a headless Firefox instance and navigate to the URL provide. Then returns the Firefox instance
    :param url: URL to send browser to
    :return: The Browser object
    """
    browser_options = Options()
    browser_options.add_argument("--headless")
    browser_options.set_preference("media.autoplay.default", 0)
    browser = webdriver.Firefox(options=browser_options)
    if url is not None:
        browser.get(url)
    return browser


def manage_threads(instances, live_video_urls: list[str]) -> None:
    for thread in instances:
        if thread[0] not in live_video_urls:
            instances.remove(thread)
            continue
        if not thread[1].is_alive():
            thread[1].start()


def main(url: str, timeout_sec: int = 300) -> None:
    try:
        browser_instances = []
        while True:
            live_videos = get_live_video_urls(url)
            for video in live_videos:
                browser = run_browser_instance(video)
                browser_instances.append((video, browser))

            print(browser_instances)

            # This will probably be made better by scheduling the function calls
            time.sleep(timeout_sec)
    except KeyboardInterrupt:
        quit()


if __name__ == '__main__':
    main("https://jupiter.tube/", timeout_sec=5)
