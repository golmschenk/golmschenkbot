"""
Tests the chase_bot module.
"""

from ..chase_bot import ChaseBot
import pytest

class TestSimpleChaseConnection:
    """Tests the ChaseBot class."""

    @pytest.fixture
    def chase_bot(self, request):
        """
        Creates a ChaseBot.
        """

        chase_bot = ChaseBot()

        def fin():
            """Fixture finalizer."""
            chase_bot.browser.close()

        request.addfinalizer(fin)

        return chase_bot

    def test_bot_can_login(self, chase_bot):
        """Tests that a manually activated bot can get to the chase transaction page."""
        chase_bot.login()

        assert "Chase Online - My Accounts" in chase_bot.browser.title
        assert "https://chaseonline.chase.com/MyAccounts.aspx" in chase_bot.browser.current_url

    def test_bot_can_get_to_chase_transaction_page(self, chase_bot):
        """Tests that a manually activated bot can get to the chase transaction page."""
        chase_bot.go_to_transaction_page()

        assert "Account Activity" in chase_bot.browser.title
        assert "https://chaseonline.chase.com/MyAccounts.aspx" in chase_bot.browser.current_url
