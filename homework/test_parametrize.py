from selene import browser
import pytest


@pytest.fixture(
    params=['1920x1080', '1366x768', '1536x864', '390x844', '414x896', '375x812']
)
def browser_management(request):
    browser.config.window_width = int(request.param.split('x')[0])
    browser.config.window_height = int(request.param.split('x')[1])


desktop_only = pytest.mark.parametrize(
    'browser_management', ['1920x1080', '1366x768', '1536x864'], indirect=True
)

mobile_only = pytest.mark.parametrize(
    'browser_management', ['390x844', '414x896', '375x812'], indirect=True
)


@desktop_only
def test_github_desktop(browser_management):
    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


@mobile_only
def test_github_mobile(browser_management):
    browser.open('https://github.com')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
