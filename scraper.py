import requests
from bs4 import BeautifulSoup
import smtplib 

URL = "https://www.amazon.com/Apple-iPhone-6S-Unlocked-64GB/dp/B01CR1AA90/ref=sr_1_3?keywords=iphone+6s&qid=1564308269&s=gateway&sr=8-3"

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id = "productTitle").get_text()
    price = soup.find(id = "priceblock_ourprice").get_text()
    converted_price = float(price[0:5])

    if(converted_price < 1.70):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 1.70):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('stephenojwang1040@gmail.com', 'cqoaqhsizvicsdzu')

    subject = 'Price fell down!'
    body = 'Check the Amazon link to see prices: https://www.amazon.com/Apple-iPhone-6S-Unlocked-64GB/dp/B01CR1AA90/ref=sr_1_3?keywords=iphone+6s&qid=1564308269&s=gateway&sr=8-3'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'stephenojwang1040@gmail.com',
        'stephenochieng001@yahoo.com',
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()

check_price()

