"""
Tests the overall bot functionality for Simple to Chase interactions.
"""

from chase_bot import ChaseBot
import pytest
from selenium import webdriver

class TestSimpleChaseConnection():
    """Tests the interactions between Simple and Chase bank from Greg's point of view."""

    def test_bot_can_get_to_chase_transaction_page(self, fixture_safari):
        """Tests that a manually activated bot can get to the chase transaction page."""
        chase_bot = ChaseBot()

        chase_bot.go_to_transaction_page()

        assert "Account Activity" in chase_bot.driver.title
        assert "https://chaseonline.chase.com/MyAccounts.aspx" in chase_bot.driver.current_url
