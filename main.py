import os
import time

import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.webdriver import WebDriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService


def get_live_video_urls(instance_url: str) -> list[str]:
    """
    Get a list of URLs for the videos that are currently live.
    :param instance_url: base url of the PeerTube instance that will be called
    :return: list of URLs as strings
    """
    search_url: str = f"{instance_url}api/v1/search/videos?isLive=true&sort=-publishedAt"
    videos_json: dict = requests.get(search_url).json()
    return [v["url"] for v in videos_json["data"]]


def run_browser_instance(url: str = None) -> WebDriver:
    """
    Create a headless Firefox instance and navigate to the URL provide. Then returns the Firefox instance
    :param url: URL to send browser to
    :return: The Browser object
    """
    browser_options: Options = Options()
    browser_options.add_argument("-headless")
    browser_options.set_preference("media.autoplay.default", False)
    browser: WebDriver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()),
                                           options=browser_options)
    if url is not None:
        browser.get(url)
    return browser


def main(url: str, api_call_interval_sec: int) -> None:
    browser_instances: list[tuple[str, WebDriver]] = []
    while True:
        print("Checking for live videos")
        live_videos: list[str] = get_live_video_urls(url)

        print(f"Current live videos: {len(live_videos)}")
        for (url, browser) in browser_instances:
            if url not in live_videos:
                print(f"{url} is no longer live. Closing browser session")
                browser.close()

        for video in live_videos:
            if video not in (i[0] for i in browser_instances):
                browser: WebDriver = run_browser_instance(video)
                browser_instances.append((video, browser))

        # This will probably be made better by scheduling the function calls
        time.sleep(api_call_interval_sec)


if __name__ == '__main__':
    api_url: str = os.getenv("peertube_url", default="https://jupiter.tube/")
    api_call_interval: int = int(os.getenv("ping_interval", default="300"))
    main(api_url, api_call_interval)
