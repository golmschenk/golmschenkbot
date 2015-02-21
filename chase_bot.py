"""
Module for bot to Chase interaction.
"""

from selenium import webdriver
from secret import Secret
from gmail_bot import GmailBot

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChaseBot:
    """
    Bot class for Chase interactions.
    """

    def __init__(self):
        self.browser = webdriver.Firefox()

    def handle_unknown_computer(self):
        """
        If the computer is unknown, Chase wants to make sure it's really you. This function handles that.
        :return:
        """
        self.browser.find_element_by_id("NextButton").click()
        self.browser.find_element_by_id("usrCtrlOtp_rdoDelMethod1").click()
        self.browser.find_element_by_id("NextButton").click()
        code = GmailBot().get_identification_code()
        password_input = self.browser.find_element_by_id("usrCtrlOtp_txtActivationCode")
        password_input.send_keys(code)
        password_input = self.browser.find_element_by_id("usrCtrlOtp_txtPassword")
        password_input.send_keys(Secret.chase_password)
        self.browser.find_element_by_id("NextButton").click()

    def login(self):
        """
        Logs the user in.
        :return:
        """
        self.browser.get("https://chaseonline.chase.com/")
        username_input = self.browser.find_element_by_id("UserID")
        username_input.send_keys(Secret.chase_username)
        password_input = self.browser.find_element_by_id("Password")
        password_input.send_keys(Secret.chase_password)
        self.browser.find_element_by_id('logon').click()

        # Wait for either the account or unknown computer page to load.
        wait = WebDriverWait(self.browser, 10)
        wait.until(AnyEc(EC.title_contains("Chase Online - My Accounts"), EC.title_contains("Chase Online - Instructions")))

        if "Chase Online - Instructions" in self.browser.title:
            self.handle_unknown_computer()

    def go_to_transaction_page(self):
        """
        Opens the transaction activity page from the user homepage.
        """
        self.browser.find_element_by_partial_link_text("See activity").click()
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.title_contains("Account Activity"))

    def get_transactions(self):
        transactions = []
        pending_div = self.browser.find_element_by_id("Pending") # TODO - Check that it actually exists
        pending_table = pending_div.find_element_by_class_name("card-activity")
        pending_rows = pending_table.find_elements_by_class_name("summary")
        for pending_row in pending_rows:
            row_data = pending_row.find_elements_by_tag_name("td")
            transaction = {"date": row_data[1].innerHTML,
                           "description": row_data[4].get_element_by_tag_name("span").innerHTML,
                           "amount": row_data[5].innerHTML}
            transactions.append(transaction)
        return transactions

class AnyEc:
    """ Use with WebDriverWait to combine expected_conditions
        in an OR.
    """
    def __init__(self, *args):
        self.ecs = args

    def __call__(self, driver):
        for fn in self.ecs:
            try:
                if fn(driver): return True
            except:
                pass