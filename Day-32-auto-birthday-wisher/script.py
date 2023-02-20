import smtplib
import os
import pandas
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("password")
email = os.getenv("email")


# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=email, password=password)
#     connection.sendmail(
#         from_addr=email,
#         to_addrs="mir.hm110@gmail.com",
#         msg="Subject: Testing ABW \n\n Ami Mir Hussain Bolchi")

birthday_data = pandas.read_csv("./birthday-sheet.csv")


with open(f"./letter_templates/letter_{1}.txt") as file:
    letter = file.read()
    print(letter)
