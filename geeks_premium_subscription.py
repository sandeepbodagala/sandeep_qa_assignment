import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#CONSTANTS
USERNAME = "sandeep.bodagala@gmail.com"
PASSWORD = "Sandy@123"
CARDNO = "4748467843517004"
EXPIRYMONTH = "11/26"
CVV = "333"

#Intializing webdriver
driver = webdriver.Chrome()
driver.get("https://www.geeksforgeeks.org/")
driver.maximize_window()
driver.implicitly_wait(13)

#Sign in Page
driver.find_element(By.XPATH,"//button[text() = 'Sign In']").click()
driver.find_element(By.CSS_SELECTOR,"input[class='mb15 next_input ']").send_keys(USERNAME)
driver.find_element(By.CSS_SELECTOR,"input[class='next_input ']").send_keys(PASSWORD)
driver.find_element(By.CSS_SELECTOR,"button[title='Sign In']").click()

#Skipping the user type
wait = WebDriverWait(driver,10)
element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[@class='skipButton_head__JLxTC']")))
element.click()

#Taking premium subscription
#click on premium
fields = driver.find_elements(By.XPATH,"//a[@class='SearchChip_searchChip__oKfVN']")
for field in fields:
    if field.text == "Go Premium":
        field.click()
        break

#switching to new window
windowsOpened = driver.window_handles
driver.switch_to.window(windowsOpened[1])

#taking premius sub
driver.find_element(By.CSS_SELECTOR,"button[class = 'ui button premium_premium_cta__8iSd_ ']").click()
waits = WebDriverWait(driver,20)
command = waits.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"div[class='premium_card__lje__ '] button[type='button']")))
command.click()

#click payment option
driver.find_element(By.CSS_SELECTOR,"button[class = 'ui fluid button premium_pay_now_cta__N2BqV']").click()

#switching to payment frame
iframes = driver.find_elements(By.CLASS_NAME, "razorpay-checkout-frame")
driver.switch_to.frame(iframes[0])

#selecting card
waiting = WebDriverWait(driver, 20)
card = waiting.until(expected_conditions.element_to_be_clickable((By.CSS_SELECTOR,"div[data-value='card']")))
card.click()

#Entering card details
driver.find_element(By.CSS_SELECTOR,"input[placeholder='Card Number']").send_keys(CARDNO)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='MM / YY']").send_keys(EXPIRYMONTH)
driver.find_element(By.CSS_SELECTOR,"input[placeholder='CVV']").send_keys(CVV)
driver.find_element(By.CSS_SELECTOR,"input[name='save']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Continue']").click()
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Skip OTP']").click()
time.sleep(10)