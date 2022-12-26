import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import ElementClickInterceptedException


#initialize global variables
PATH = '~/.local/bin/chromedriver'
INSTAGRAM_UNAME = os.getenv('INSTAGRAM_UNAME')
INSTAGRAM_PW = os.getenv('INSTAGRAM_PW')
FOLLOW_ACCOUNT = 'hackthebox'


class InstaFollower:
    def __init__(self, path):
        self.options = Options()
        self.options.add_experimental_option("debuggerAddress", "127.0.0.1:9014")
        self.driver = webdriver.Chrome(PATH, options=self.options)
        #if not in debugger mode
        # self.driver.set_window_position(207, 1218)
        # self.driver.maximize_window()


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        
        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(INSTAGRAM_UNAME)
        password.send_keys(INSTAGRAM_PW)

        sleep(2)
        password.send_keys(Keys.ENTER)


    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{FOLLOW_ACCOUNT}")

        sleep(2)
        followers = self.driver.find_element(By.CSS_SELECTOR, 'li a div span')
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.CLASS_NAME, '_aano')
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(4)
            bot.follow()


    def follow(self):
        sleep(3)
        all_buttons = self.driver.find_elements(By.CLASS_NAME, "_acas")
        for button in all_buttons:
            try:
                button.click()
                sleep(3)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.CSS_SELECTOR, 'div div button div svg')
                cancel_button.click()


bot = InstaFollower(PATH)
# bot.login()
bot.find_followers()

