from selenium.webdriver.common.by import By

class LoginPage:
    URL = "https://staging.megashop.example/login"
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "loginBtn")
    PROFILE_ICON = (By.ID, "profileIcon")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, email, password):
        self.driver.find_element(*self.EMAIL).clear()
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.PASSWORD).clear()
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BTN).click()

    def is_logged_in(self):
        return len(self.driver.find_elements(*self.PROFILE_ICON)) > 0
