import pytest
from selene import browser, be


@pytest.fixture(
    params=['1920x1080', '1366x768', '1536x864', '390x844', '414x896', '375x812']
)
def browser_management(request):
    if request.param in ['1920x1080', '1366x768', '1536x864']:
        width, height = map(int, request.param.split('x'))
        browser.config.window_width = width
        browser.config.window_height = height
        yield 'desktop'
    elif request.param in ['390x844', '414x896', '375x812']:
        width, height = map(int, request.param.split('x'))
        browser.config.window_width = width
        browser.config.window_height = height
        yield 'mobile'

    browser.quit()


def test_github_desktop(browser_management):
    if browser_management == 'mobile':
        pytest.skip(reason='Не запускаем mobile')

    browser.open('https://github.com')
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()


def test_github_mobile(browser_management):
    if browser_management == 'desktop':
        pytest.skip(reason='Не запускаем desktop')

    browser.open('https://github.com')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').should(be.clickable).click()
