"""
Module for bot to Chase interaction.
"""

from selenium import webdriver
from secret import Secret
from gmail_bot import GmailBot

class ChaseBot:
    """
    Bot class for Chase interactions.
    """

    def __init__(self):
        self.browser = webdriver.Chrome()

    def handle_unknown_computer(self):
        """
        If the computer is unknown, Chase wants to make sure it's really you. This function handles that.
        :return:
        """
        self.browser.find_element_by_id("NextButton").click()
        self.browser.find_element_by_id("usrCtrlOtp_rdoDelMethod1").click()
        self.browser.find_element_by_id("NextButton").click()
        code = GmailBot.get_identification_code()
        password_input = self.browser.find_element_by_id("usrCtrlOtp_txtActivationCode")
        password_input.send_keys(code)
        password_input = self.browser.find_element_by_id("usrCtrlOtp_txtPassword")
        password_input.send_keys(Secret.chase_password)
        self.browser.find_element_by_id("NextButton").click()


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

        if "Chase Online - Instructions" in self.browser.title:
            self.handle_unknown_computer()
