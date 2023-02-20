import smtplib
import os
import pandas
import random
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
birthday_list = [{**row}
                 for _, row in birthday_data.iterrows()]

print(birthday_list)

letter_number = random.randint(1, 3)
with open(f"./letter_templates/letter_{letter_number}.txt") as file:
    content = file.read()
