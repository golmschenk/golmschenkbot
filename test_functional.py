"""
Tests the overall bot functionality.
"""

import pytest
from selenium import webdriver

class TestSimpleChaseConnection():
    """Tests the interactions between Simple and Chase bank from Greg's point of view."""

    @pytest.fixture
    def fixture_chrome(self, request):
        """
        Sets up the chrome browser.
        :param request: The pytest request object.
        """
        # Start PhantomJS browser.
        self.browser = webdriver.PhantomJS()

        def fin():
            """Fixture finalizer."""
            self.browser.quit()

        request.addfinalizer(fin)

    #def test_homepage_visit(self, fixture_chrome):
    #    """Test that the homepage loads."""
    #    self.browser.get('http://localhost:8080')
    #    assert 'Crowd Navigation' in self.browser.title