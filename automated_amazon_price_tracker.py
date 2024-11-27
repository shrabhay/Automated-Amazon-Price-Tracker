import requests
from bs4 import BeautifulSoup
import smtplib
import os
os.system('clear')

LIVE_URL = ('https://www.amazon.in/PHILIPS-Digital-HD9252-90-Technology/dp/B097RJ867P/ref=sr_1_4?crid=162L8P0YFW2L6&dib'
            '=eyJ2IjoiMSJ9.DEDIRPddVqVS6sMci0Xk6u2zTHjLpCvAGYbdukNdJR'
            '-H65Z3vek3Ovne9xJhXRHFQCosR6uhAXTP4dKDtMHXIArXNuQ8ZZH3SNo9ayWxvJvvIP6NJ4zwZLccmap_RvtNIC5GY7HCxLXdDYyOpez'
            'XGCHlLkIb4R7gz2FAy8SeXrGRelDlIALJXDoL2eCobCioR97Dscx3mnkU85tQ1Hpfjg9WNHafKPJlQrPDVM2Mhp0.3kNXgo48a1mEmVw'
            '3mrfmv9qn4z4_bQdmlBg4PEUJc24&dib_tag=se&keywords=air%2Bfryer&qid=1727962255&sprefix=air%2Bf%2Caps%2C270'
            '&sr=8-4&th=1')
TEST_URL = 'https://appbrewery.github.io/instant_pot/'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/129.0.0.0 Safari/537.36',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6'
}


def connect_to_email_account():
    connection = smtplib.SMTP(host='smtp.gmail.com')
    connection.starttls()
    connection.login(
        user='<YOUR_EMAIL_ADDRESS>',
        password='<YOUR_EMAIL_PASSWORD>'
    )
    return connection


def send_price_alert(actual_price, product_title):
    sender_email = '<SENDER EMAIL'
    recipient_emails = '<RECEIVER EMAIL'

    subject = 'Amazon Price Alert'
    message = f'{product_title} is now ₹{actual_price}. Buy Now!!\n{LIVE_URL}'

    connection = connect_to_email_account()
    connection.sendmail(
        from_addr=sender_email,
        to_addrs=recipient_emails,
        msg=f'Subject:{subject}\n\n{message}'.encode('utf-8')
    )
    connection.close()


response = requests.get(url=LIVE_URL, headers=HEADERS)
amazon_webpage = response.text
soup = BeautifulSoup(amazon_webpage, 'html.parser')
# print(soup)

whole_price = float(soup.find(name='span', class_='a-price-whole').getText().split('.')[0].replace(',', ''))
product = soup.select_one(selector='#productTitle').getText().strip()
product = ' '.join(product.split())

if whole_price < 8500:
    send_price_alert(actual_price=whole_price, product_title=product)
