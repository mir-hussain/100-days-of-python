import requests
import smtplib
import os
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

email = os.getenv("email")
password = os.getenv("pass")

TARGET_PRICE = 563

user_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

url = "https://www.amazon.com/Intel-i9-13900KF-Desktop-Processor-P-cores/dp/B0BCFM3CJ4/?_encoding=UTF8&pd_rd_w=zW0KJ&content-id=amzn1.sym.10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_p=10f16e90-d621-4a53-9c61-544e5c741acc&pf_rd_r=FZM58TWSNF8ZR2G35W1C&pd_rd_wg=Tih58&pd_rd_r=972f80d5-6c30-4625-b1e2-d5ba6c7ed5ee&ref_=pd_gw_exports_top_sellers_unrec"

res = requests.get(url=url, headers=user_headers)
res.raise_for_status()


soup = BeautifulSoup(res.text, "html.parser")

price = int(
    soup.find(class_="a-price-whole").get_text(strip=True).replace(".", ""))

if price <= TARGET_PRICE:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email,
                         password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject: Price alert\n\n Hey product price drop below your target price. {url}"
        )
        print(f"Mail send")
