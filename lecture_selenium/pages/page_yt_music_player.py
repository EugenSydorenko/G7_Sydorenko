from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class PageYTMusic:
    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.band_loc = f'//a[text()="{band}"]'
        self.song_locator = '//ancestor::ytmusic-responsive-list-item-renderer' \
                            '//a[contains(@href, "watch")]'
        self.all_songs_locator = (By.XPATH, f'{self.band_loc}{self.song_locator}')

        elements = (By.XPATH, self.all_songs_locator)
        song_names = [el.text for el in elements]

    def any(self):
        self.driver.get('https://')

PageYTMusic()
