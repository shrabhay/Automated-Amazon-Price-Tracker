# Automated Amazon Price Tracker
## Description
This Python script allows users to track the price of a product on Amazon and sends an email alert when the price drops below a specified threshold. It uses BeautifulSoup for web scraping and smtplib for sending email notifications.

---

## Features
* Tracks the price of a specific product on Amazon.
* Sends an email alert when the product price is below the defined threshold.
* Easy to set up and customize.

---

## Prerequisites
* Python 3.x installed on your system.
* An Amazon product URL.
* SMTP credentials to send email notifications.

---

## Installation
1. Clone this repository:
    ```commandline
    git clone https://github.com/shrabhay/Automated-Amazon-Price-Tracker.git
    cd Automated-Amazon-Price-Tracker
    ```

2. Install the required Python packages:
    ```commandline
    pip install requests
    pip install bs4
    pip install smtplib
    ```

3. Add your email credentials and product details to the script:
* Replace `<YOUR_EMAIL_ADDRESS>` and `<YOUR_EMAIL_PASSWORD>` in the `connect_to_email_account()` function.
* Replace `<SENDER EMAIL>` and `<RECEIVER EMAIL>` in the `send_price_alert()` function.
* Replace the `LIVE_URL` with the Amazon product URL you want to track.
* Ensure the correct User-Agent is provided in the `HEADERS` dictionary to avoid being blocked by Amazon.

---

## SMTP Setup
To send email alerts, you need to configure an SMTP server. Below are the steps for setting up Gmail as your SMTP server:

### For Gmail Users
* Go to Google Account Security.
* Enable 2-Step Verification.
* Create an App Password:
  * Under Signing in to Google, select App Passwords.
  * Choose the app (e.g., "Mail") and device (e.g., "Other (Custom name): Price Tracker") for which you're generating the password.
  * Copy the 16-character password generated by Google.
* Replace <YOUR_EMAIL_PASSWORD> in the script with the generated App Password.

### For Other Email Providers
Refer to your email provider’s documentation to get SMTP server details and configure App Passwords or authentication methods.

---

## Usage
1. Run the script:
    ```commandline
    python3 automated_amazon_price_tracker.py
    ```

2. The script will scrape the product's price and send an email alert if the price falls below the set threshold (`8500` in the example).

---

## Customization
* **Price Threshold**: Update the `if whole_price < 8500:` condition with your desired threshold.
* **Product URL**: Replace `LIVE_URL` with the Amazon product URL of your choice.

---

## Disclaimer
* Amazon may block requests from automated scripts if too many requests are made. Use the script responsibly.
* Always comply with Amazon's Terms of Service when using this script.

---

## Contributions
Feel free to submit a pull request or raise issues for improvements or bug fixes.

---

## License
This project is licensed under the MIT License.