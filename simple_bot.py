"""
Module for bot to Simple interaction.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from secret import Secret


class SimpleBot:
    """
    Bot class for Simple interactions.
    """
    def __init__(self):
        self.browser = webdriver.Firefox()

    def login(self):
        """
        Goes to the transactions page.
        :return:
        """
        self.browser.get("https://bank.simple.com/signin")
        username_input = self.browser.find_element_by_id("login_username")
        username_input.send_keys(Secret.simple_username)
        password_input = self.browser.find_element_by_id("login_password")
        password_input.send_keys(Secret.simple_password)
        self.browser.find_element_by_id('signin-btn').click()

    def go_to_transfer(self):
        self.browser.find_element_by_id("send-money-btn").click()
        self.browser.find_element_by_xpath("//*[@data-contact-type='external']").click()
        self.browser.find_element_by_xpath("//*[@data-account-id='" + Secret.simple_chase_data_account_id + "']").click()
        self.browser.find_element_by_class_name("outbound").click()


