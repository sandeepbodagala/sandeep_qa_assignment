from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class Base:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.implicitly_wait(13)

    def open_url(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()
