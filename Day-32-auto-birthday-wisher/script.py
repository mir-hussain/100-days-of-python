import smtplib
import os
import pandas
import random
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

password = os.getenv("password")
email = os.getenv("email")


birthday_data = pandas.read_csv("./birthday-sheet.csv")
birthday_list = [{**row}
                 for _, row in birthday_data.iterrows()]

for info in birthday_list:
    print(info)

    date = dt.datetime.now()

    if date.month == info["month"] and date.day == info["day"]:
        letter_number = random.randint(1, 3)
        with open(f"./letter_templates/letter_{letter_number}.txt") as file:
            content = file.read().replace("[NAME]", info["name"])

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=info["email"],
                msg=f"Subject: Wishing you Happy Birthday\n\n{content}")
