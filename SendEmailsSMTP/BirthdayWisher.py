import datetime as dt
import pandas as pd
import random
import smtplib

today = (dt.datetime.now().month, dt.datetime.now().day)

df = pd.read_csv("birthdays.csv")
birthdays_dict = {(row.month, row.day): row for (index, row) in df.iterrows()}

if today in birthdays_dict:
    letter_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file=letter_path) as file:
        contents = file.read()
        contents = contents.replace("[NAME]", birthdays_dict[today]["name"])

    my_email = "gizat.m@yahoo.com"
    my_password = "vhfsvlrtqewoxgvm"

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthdays_dict[today]["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}")
