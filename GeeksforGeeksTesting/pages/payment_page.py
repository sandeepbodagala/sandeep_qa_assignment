from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class PaymentPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.card_option = (By.CSS_SELECTOR, "div[data-value='card']")
        self.card_number_field = (By.CSS_SELECTOR, "input[placeholder='Card Number']")
        self.expiry_field = (By.CSS_SELECTOR, "input[placeholder='MM / YY']")
        self.cvv_field = (By.CSS_SELECTOR, "input[placeholder='CVV']")
        self.save = (By.CSS_SELECTOR, "input[name='save']")
        self.continue_btn = (By.XPATH, "//button[text()='Continue']")
        self.pay_now_botton = "button[class = 'ui fluid button premium_pay_now_cta__N2BqV']"
        self.razor_pay_class = (By.CLASS_NAME, "razorpay-checkout-frame")
        self.card_field = (By.CSS_SELECTOR, "div[data-value='card']")
        self.skip_otp = (By.XPATH, "//button[text()='Skip OTP']")
        self.error_message = (By.XPATH, "//span[text() = 'Please enter a valid card number']")

    def go_to_payment_option(self):
        command = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.pay_now_botton)))
        command.click()

        iframes = self.driver.find_elements(*self.razor_pay_class)
        self.driver.switch_to.frame(iframes[0])

        card = self.wait.until(EC.element_to_be_clickable((self.card_field)))
        card.click()

    def enter_card_details(self, cardno, expiry, cvv):
        self.wait.until(EC.element_to_be_clickable(self.card_option)).click()
        self.driver.find_element(*self.card_number_field).send_keys(cardno)
        self.driver.find_element(*self.expiry_field).send_keys(expiry)
        self.driver.find_element(*self.cvv_field).send_keys(cvv)
        self.driver.find_element(*self.save).click()
        time.sleep(1)
        self.driver.find_element(*self.continue_btn).click()
        time.sleep(1)
        self.driver.find_element(*self.skip_otp).click()
        time.sleep(10)

    def enter_invalid_card_details(self, cardno, expiry, cvv):
        self.wait.until(EC.element_to_be_clickable(self.card_option)).click()
        self.driver.find_element(*self.card_number_field).send_keys(cardno)
        self.driver.find_element(*self.expiry_field).send_keys(expiry)
        self.driver.find_element(*self.cvv_field).send_keys(cvv)
        self.driver.find_element(*self.error_message)
        time.sleep(2)