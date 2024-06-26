import pytest
from selene import browser


@pytest.fixture(params=['1920x1080', '1366x768', '1536x864'])
def desktop_screen_resolution(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=['390x844', '414x896', '375x812'])
def mobile_screen_resolution(request):
    width, height = map(int, request.param.split('x'))
    browser.config.window_width = width
    browser.config.window_height = height


def test_github_desktop(desktop_screen_resolution):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(mobile_screen_resolution):
    browser.open('https://github.com')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
