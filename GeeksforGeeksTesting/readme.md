
# Automation Framework for Subscription Flow

## Overview
This project implements an automation framework using the Page Object Model (POM) to automate the subscription flow on a website. It covers the login, premium subscription, and payment steps.

## Prerequisites
- Python 3.x installed on your system.
- Google Chrome browser installed.
- ChromeDriver matching your browser version installed.

## Setup Instructions

### 1. Clone the repository
Clone the project repository to your local machine:
```bash
git clone <repository_url>
```

### 2. Install dependencies
Navigate to the project folder and install the required dependencies:
```bash
cd <project_folder>
pip install -r requirements.txt
```

This will install the following dependencies:
- `selenium`: For automating the web browser.
- `pytest`: For running and managing test cases.

### 3. Configuration
The following constants are stored in the `utils/config.py` file:
- USERNAME: Your email for login.
- PASSWORD: Your password for login.
- CARDNO: Card number for payment.
- EXPIRYMONTH: Card expiry month and year.
- CVV: Card CVV number.
- URL: The website URL to automate.

Make sure these details are correct for the automation to work properly.


## Running the Test

To run the test for the subscription flow, use `pytest`:
```bash
pytest tests/test_subscription.py
or
pytest tests
```

### Test Execution
- The test will automatically open the website, log in using the provided credentials, select the premium subscription, and complete the payment process with the provided card details.
- The test waits for elements to load dynamically and interacts with the page accordingly.

