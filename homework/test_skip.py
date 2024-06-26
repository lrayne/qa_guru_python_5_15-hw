import pytest
from selene import browser


@pytest.fixture(
    params=['1920x1080', '1366x768', '1536x864', '390x844', '414x896', '375x812']
)
def browser_management(request):
    browser.config.window_width = int(request.param.split('x')[0])
    browser.config.window_height = int(request.param.split('x')[1])
    return request.param


def test_github_desktop(browser_management):
    if browser_management in ['390x844', '414x896', '375x812']:
        pytest.skip(reason='Не запускаем mobile')

    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_github_mobile(browser_management):
    if browser_management in ['1920x1080', '1366x768', '1536x864']:
        pytest.skip(reason='Не запускаем desktop')

    browser.open('https://github.com')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
