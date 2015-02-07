"""
Module for bot to Chase interaction.
"""

from selenium import webdriver
from secret import Secret

class ChaseBot:
    """
    Bot class for Chase interactions.
    """

    def __init__(self):
        self.browser = webdriver.Chrome()

    def login(self):
        """
        Goes to the transactions page.
        :return:
        """
        self.browser.get("https://www.chase.com")
        username_input = self.browser.find_element_by_id("usr_name_home")
        username_input.send_keys(Secret.chase_username)
        password_input = self.browser.find_element_by_id("usr_password_home")
        password_input.send_keys(Secret.chase_password)
        self.browser.find_element_by_xpath("//a[@data-pt-name='unknwnlogin']").click()