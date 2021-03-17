import pandas
import datetime as dt
import smtplib
import random

my_email = "fryphilip99@yahoo.com"
password = "foalcvfybucuxgrf"

today = (dt.datetime.now().month, dt.datetime.now().day)
birthdays = pandas.read_csv("birthdays.csv")

birthdays_dict = {(row.month, row.day): row for (index, row) in birthdays.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt") as wish_file:
        wish_mail = wish_file.read().replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=birthday_person["email"], 
            msg=f"Subject:Happy Birthday\n\n{wish_mail}"
        )
        print(wish_mail)