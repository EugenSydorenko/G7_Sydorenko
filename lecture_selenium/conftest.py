from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import pytest


@pytest.fixture(scope='class')
def yt_music_page():
    my_service = Service(executable_path=ChromeDriverManager().install())
    driver = Chrome(service=my_service)
    driver.get('https://music.youtube.com/playlist?list=RDCLAK5uy_nAJDvLXRZVjXclL2N3IjoCceuaM5T7o6Q')
    yield driver
    driver.quit()


@pytest.fixture(scope='class')
def chrome(request):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-gpu')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(30)
    if request.cls:
        request.cls.__driver = driver
    yield driver
    driver.quit()
