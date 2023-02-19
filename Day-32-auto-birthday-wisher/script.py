import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("password")
email = os.getenv("email")


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    connection.sendmail(
        from_addr=email,
        to_addrs="mir.hm110@gmail.com",
        msg="Subject: Testing ABW \n\n Ami Mir Hussain Bolchi")
