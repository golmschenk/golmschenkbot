"""
Unit(ish) tests the gmail_bot module.
"""

from ..gmail_bot import GmailBot

class TestGmailBot:
    """
    Tests for the GmailBot class.
    """

    @pytest.fixture
    def gmail_bot(self):
        """
        Creates a GmailBot.
        """
        return GmailBot()

    def test_can_reach_inbox(self, gmail_bot):
        """
        Test that the bot can reach the inbox.
        :param gmail_bot:
        :return:
        """
        gmail_bot.login()

        assert "Gmail" in gmail_bot.browser.title
        assert "https://mail.google.com/mail/#inbox" in gmail_bot.browser.current_url
