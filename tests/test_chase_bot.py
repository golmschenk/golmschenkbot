"""
Tests the chase_bot module.
"""

from ..chase_bot import ChaseBot
import pytest

class TestSimpleChaseConnection:
    """Tests the ChaseBot class."""

    def test_bot_can_login(self):
        """Tests that a manually activated bot can get to the chase transaction page."""
        chase_bot = ChaseBot()

        chase_bot.login()

        assert "Chase Online - My Accounts" in chase_bot.browser.title
        assert "https://chaseonline.chase.com/MyAccounts.aspx" in chase_bot.browser.current_url

    def test_bot_can_get_to_chase_transaction_page(self):
        """Tests that a manually activated bot can get to the chase transaction page."""
        chase_bot = ChaseBot()

        chase_bot.go_to_transaction_page()

        assert "Account Activity" in chase_bot.browser.title
        assert "https://chaseonline.chase.com/MyAccounts.aspx" in chase_bot.browser.current_url
