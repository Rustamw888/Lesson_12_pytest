"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene import have
from selene.support.shared import browser

browser_size_value = pytest.fixture(params=[(1920, 1080), (360, 640)])
base_url = 'https://github.com/'


@browser_size_value
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def set_up(browser_size):
    width = browser_size.param[0]
    height = browser_size.param[1]
    browser.driver.set_window_size(width=width, height=height)
    browser.open(base_url)
    '''
    OR:     
    browser.config.window_width = width
    browser.config.window_height = height
    '''


@pytest.mark.parametrize("browser_size", [(1920, 1080)], indirect=True)
def test_github_desktop(browser_size):
    browser.element('[href="/login"]').click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_size", [(360, 640)], indirect=True)
def test_github_mobile(browser_size):
    browser.element('button[aria-label="Toggle navigation"]').click()
    browser.element('a[href="/login"]').click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))
