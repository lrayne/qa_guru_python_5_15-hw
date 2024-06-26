import pytest
from selene import browser


@pytest.fixture(params=['1920x1080', '1366x768', '1536x864'])
def desktop_screen_resolution(request):
    browser.config.window_width = int(request.param.split('x')[0])
    browser.config.window_height = int(request.param.split('x')[1])


@pytest.fixture(params=['390x844', '414x896', '375x812'])
def mobile_screen_resolution(request):
    browser.config.window_width = int(request.param.split('x')[0])
    browser.config.window_height = int(request.param.split('x')[1])


def test_github_desktop(desktop_screen_resolution):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(mobile_screen_resolution):
    browser.open('https://github.com')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
