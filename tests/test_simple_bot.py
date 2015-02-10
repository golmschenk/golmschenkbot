"""
Tests the simple_bot module.
"""

from ..simple_bot import SimpleBot
import pytest

class TestSimpleBot:
    """Tests the SimpleBot class."""

    @pytest.fixture
    def simple_bot(self, request):
        """
        Creates a SimpleBot.
        """

        simple_bot = SimpleBot()

        def fin():
            """Fixture finalizer."""
            simple_bot.browser.close()

        request.addfinalizer(fin)

        return simple_bot

    def test_bot_can_login(self, simple_bot):
        """Tests that a manually activated bot can get to the simple transaction page."""
        simple_bot.login()

        assert "Activity | Simple" in simple_bot.browser.title
        assert "https://bank.simple.com/activity" in simple_bot.browser.current_url