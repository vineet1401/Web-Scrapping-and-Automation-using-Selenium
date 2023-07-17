from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


USERNAME = "Your Username or Gmail"
PASSWORD = "Your Password"
DRIVER_PATH  = ""

SIMILAR_ACCOUNT = "buzzfeedtasty"



class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.implicitly_wait(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        self.driver.implicitly_wait(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        self.driver.implicitly_wait(5)
        self.driver.get("https://www.instagram.com/direct/t/105131134466085/")

        self.driver.implicitly_wait(2)

        self.driver.implicitly_wait(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            self.driver.implicitly_wait(2)

    def follow(self):
        all_buttons = self.driver.find_element(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                self.driver.implicitly_wait(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

bot = InstaFollower(DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()
