from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep


class SauceAutomation:
    #initializing constructor and passing url
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    
    #defining start method to maximize and get the url
    def start_automation(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(3)
        return True
    
    #to close the window
    def shutdown(self):
        self.driver.quit()

    #to fetch the title from the webpage
    def fetch_title(self):
        if self.start_automation():
            return self.driver.title
        else:
            return False

    #to fetch the required url    
    def fetch_url(self):
        if self.start_automation():
            return self.driver.current_url
        else:
            return False

    #to fetch the page content     
    def fetch_page_content(self):
        if self.start_automation():
            return self.driver.page_source
        else:
            return False
