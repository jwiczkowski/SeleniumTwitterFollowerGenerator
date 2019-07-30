from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time


class TwitterBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.chop = webdriver.ChromeOptions()
        self.chop.add_extension('/Users/jacekwiczkowski/Downloads/GoodTwitter.crx')
        self.driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', options=self.chop)

    def login(self):
        driver = self.driver
        driver.get("https://twitter.com/")
        email = driver.find_element_by_class_name("email-input")
        password = driver.find_element_by_name("session[password]")

        email.send_keys(self.username)
        password.send_keys(self.password)

        password.send_keys(Keys.RETURN)

        time.sleep(3)

    def like_tweet(self, hashtag):
        driver = self.driver
        driver.get("https:twitter.com/search?q=" + hashtag + "&src=typd")
        time.sleep(3)
        for i in range(1, 3):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(2)
            tweets = driver.find_elements_by_class_name("tweet")
            links = [test.get_attribute('data-permalink-path') for test in tweets]
            for link in links:
                driver.get("https://twitter.com" + link)
                try:
                    driver.find_element_by_class_name("HeartAnimation").click()
                    time.sleep(2)
                except Exception as ex:
                    time.sleep(5)




# insert email, and password
bot = TwitterBot()
bot.login()

# insert hashtag to like tweets
bot.like_tweet()
