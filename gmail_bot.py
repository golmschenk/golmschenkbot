"""
Module for bot for Gmail interaction.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from secret import Secret
import re


class GmailBot:
    """
    Bot class for Gmail interactions.
    """

    def __init__(self):
        self.browser = webdriver.Chrome()

    def login(self):
        """
        Goes to the inbox page.
        :return:
        """
        self.browser.get("https://mail.google.com/")
        username_input = self.browser.find_element_by_id("Email")
        username_input.send_keys(Secret.gmail_username)
        password_input = self.browser.find_element_by_id("Passwd")
        password_input.send_keys(Secret.gmail_password)
        self.browser.find_element_by_id("signIn").click()

    def open_first_email(self):
        """
        Opens the first email in gmail.
        :return:
        """
        self.browser.find_element_by_xpath("//*[contains(text(), 'Your Requested Online Banking Identification Code')]").click()

    def extract_code(self):
        text_element = self.browser.find_element_by_class_name("msg")
        text = text_element.get_attribute("innerHTML")
        code = re.search(re.compile(r"Your Identification Code is: ([0-9]+)"), text).group(1)
        return code

    def get_identification_code(self):
        self.login()
        self.open_first_email()
        return self.extract_code()
