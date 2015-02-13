"""
Unit(ish) tests the gmail_bot module.
"""

from ..gmail_bot import GmailBot
import pytest

class TestGmailBot:
    """
    Tests for the GmailBot class.
    """

    @pytest.fixture
    def gmail_bot(self, request):
        """
        Creates a GmailBot.
        """

        gmail_bot = GmailBot()

        def fin():
            """Fixture finalizer."""
            gmail_bot.browser.close()

        request.addfinalizer(fin)

        return gmail_bot

    def test_can_reach_inbox(self, gmail_bot):
        """
        Test that the bot can reach the inbox.
        :param gmail_bot:
        :return:
        """
        gmail_bot.login()

        assert "Gmail" in gmail_bot.browser.title
        assert "https://mail.google.com/mail/" in gmail_bot.browser.current_url

    def test_can_open_first_email(self, gmail_bot):
        """
        Test that the bot can reach the inbox.
        :param gmail_bot:
        :return:
        """
        gmail_bot.login()

        gmail_bot.open_first_email()

        assert "Your Requested Online Banking" in gmail_bot.browser.title

    def test_can_find_code(self, gmail_bot):
        """
        Test that the bot can reach the inbox.
        :param gmail_bot:
        :return:
        """
        gmail_bot.login()
        gmail_bot.open_first_email()

        code = gmail_bot.extract_code()

        assert code.isdigit()