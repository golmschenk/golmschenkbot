"""
Module for bot for Gmail interaction.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from secret import Secret

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
        # Wait for the asynchronous stuff to load.
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, "gba")))

    def open_first_email(self):
        """
        Opens the first email in gmail.
        :return:
        """
        self.browser.find_element_by_xpath("//*[@id=\":2v\"]/div/div/div").click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.ID, ":5h")))

    def get_identification_code(self):
        self.login()
        self.open_first_email()
        return self.extract_code()
