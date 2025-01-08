from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, wait, driver):
        self.driver = driver
        self.wait = wait
        self.sign_in_button = "//button[text()='Sign In']"
        self.email_field = (By.CSS_SELECTOR, "input[class='mb15 next_input ']")
        self.password_field = (By.CSS_SELECTOR, "input[class='next_input ']")
        self.submit_button = (By.CSS_SELECTOR, "button[title='Sign In']")

    def login(self, username, password):
        command = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button)))
        command.click()
        self.driver.find_element(*self.email_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.submit_button).click()
