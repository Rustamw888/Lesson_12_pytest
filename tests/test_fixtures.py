"""
Сделайте разные фикстуры для каждого теста
"""
import pytest
from selene import have
from selene.support.shared import browser

base_url = 'https://github.com/'


@pytest.fixture(scope='session')
def desktop():
    browser.open(base_url)
    browser.driver.set_window_size(width=1920, height=1080)
    yield
    browser.quit()


def test_github_desktop(desktop):
    browser.element('[href="/login"]').click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))


@pytest.fixture(scope='session')
def mobile():
    browser.open(base_url)
    browser.driver.set_window_size(width=360, height=640)
    yield
    browser.quit()


def test_github_mobile(mobile):
    browser.element('button[aria-label="Toggle navigation"]').click()
    browser.element('a[href="/login"]').click()
    browser.element('h1').should(have.exact_text('Sign in to GitHub'))

