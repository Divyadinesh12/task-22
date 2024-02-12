"""
using python selenium automation extract the total number of followers and following from the url
"""


from selenium import webdriver
from selenium .webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class GuviInsta:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def boot(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def get_NumberOf_Post(self):
        """
        this method display the number of post for this particular instagram id
        :return: number of post
        """
        x_path = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[1]/button/span/span"
        post = self.driver.find_element(by=By.XPATH, value=x_path).text
        print("post", post)

    def get_NumberOf_Followers(self):
        """
        this method display the number of followers
        :return: int
        """
        x_path = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button/span/span"
        followers = self.driver.find_element(by=By.XPATH, value=x_path).text
        print("followers", followers)

    def get_NumberOf_Following(self):
        """
        this method display the number of following
        :return: number of following
        """
        x_path = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button/span/span"
        following = self.driver.find_element(by=By.XPATH, value=x_path).text
        print("following", following)

    def quit(self):
        """
        this method close the driver
        :return: None
        """
        self.driver.quit()


url = "https://www.instagram.com/guviofficial/"
obj = GuviInsta(url)
obj.boot()
obj.get_NumberOf_Post()
obj.get_NumberOf_Followers()
obj.get_NumberOf_Following()