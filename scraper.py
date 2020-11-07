import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://playtech.co.nz/collections/monitors-home-business/products/gigabyte-g27qc-27-va-165hz-1440p-curved-gaming-monitor-1ms-mprt-92-dci-p3-and-120-srgb-hdr-ready-freesync-premium-g-sync-compatible-ready'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}

def scrape_price():
   
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="h2").get_text()
    price = soup.find(class_="price").get_text()

    converted = float(price[1:])


    print(title)
    print(converted)

    if (converted < 800):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo
    server.starttls()
    server.ehlo()

    server.login()

    subject = 'Price down!'
    body = 'Check here https://playtech.co.nz/collections/monitors-home-business/products/gigabyte-g27qc-27-va-165hz-1440p-curved-gaming-monitor-1ms-mprt-92-dci-p3-and-120-srgb-hdr-ready-freesync-premium-g-sync-compatible-ready'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        
        msg
        )
    print('Email sent')

    server.quit()



scrape_price()