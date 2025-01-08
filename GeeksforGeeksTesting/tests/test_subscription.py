import pytest
from utils.base import Base
from utils.config import USERNAME, PASSWORD, CARDNO, EXPIRYMONTH, CVV, URL
from pages.login_page import LoginPage
from pages.premium_page import PremiumPage
from pages.payment_page import PaymentPage

def test_subscription():
    base = Base()
    driver = base.driver
    wait = base.wait

    try:
        # Open website
        base.open_url(URL)

        # Login
        login_page = LoginPage(wait, driver)
        login_page.login(USERNAME, PASSWORD)

        # Premium subscription
        premium_page = PremiumPage(driver, wait)
        premium_page.skip_user_type()
        premium_page.select_premium()

        # Payment
        payment_page = PaymentPage(driver, wait)
        payment_page.go_to_payment_option()
        payment_page.enter_card_details(CARDNO, EXPIRYMONTH, CVV)
    finally:
        base.quit()
