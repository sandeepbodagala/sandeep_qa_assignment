Project Overview:
--------------------------
This script automates the process of signing in to GeeksforGeeks, navigating to the premium subscription section, and completing a mock payment using Selenium WebDriver.

Prerequisites
-------------------
Python installed on your system.
Google Chrome browser and the corresponding version of ChromeDriver.
Install Selenium library: pip install selenium
Constants in the Script
    Update the following constants in the script with your details:
        USERNAME: Your GeeksforGeeks username.
        PASSWORD: Your GeeksforGeeks password.
        CARDNO: Mock card number for payment.
        EXPIRYMONTH: Mock expiry date of the card.
        CVV: Mock CVV number.

How to Run
----------------
Run the script using the command:
    python geeks_premium_subscription.py


Script Workflow
-------------------
1) Opens GeeksforGeeks and maximizes the browser window.
2) Logs in with the provided credentials.
3) Skips the user type selection screen.
4) Navigates to the premium subscription page.
5) Handles the new browser window for premium subscription.
6) Selects a premium plan and proceeds to the payment page.
7) Switches to the Razorpay payment.
8) Selects the card payment option and fills in the card details.
9) Completes the payment process.

Notes
-------------------
Implicit and explicit waits are used to ensure elements are loaded before interaction.
Replace mock payment details with valid data only for real transactions.