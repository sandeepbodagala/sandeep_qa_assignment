from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class PremiumPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.go_premium_button = (By.XPATH, "//a[@class='SearchChip_searchChip__oKfVN']")
        self.skip_button = (By.XPATH, "//button[@class='skipButton_head__JLxTC']")
        self.premium_card = (By.CSS_SELECTOR, "button[class = 'ui button premium_premium_cta__8iSd_ ']")
        self.premium_card_botton = "div[class='premium_card__lje__ '] button[type='button']"

    def skip_user_type(self):
        self.wait.until(EC.element_to_be_clickable(self.skip_button)).click()

    def select_premium(self):
        fields = self.driver.find_elements(*self.go_premium_button)
        for field in fields:
            if field.text == "Go Premium":
                field.click()
                break

        windows_opened = self.driver.window_handles
        self.driver.switch_to.window(windows_opened[1])
        self.driver.find_element(*self.premium_card).click()

        time.sleep(1)
        command = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.premium_card_botton)))
        command.click()