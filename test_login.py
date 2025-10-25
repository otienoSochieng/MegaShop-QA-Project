import pytest
from selenium import webdriver
from automation.pages.login_page import LoginPage

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login('testuser@example.com', 'Password123')
    assert login.is_logged_in()
