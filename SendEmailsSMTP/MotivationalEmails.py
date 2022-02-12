import smtplib
import datetime as dt
import random


my_email = "gizat.m@yahoo.com"
my_password = "vhfsvlrtqewoxgvm"

now = dt.datetime.now()
weekdays = [0, 1, 2, 3, 4]

if now.weekday() in weekdays:
    with open("quotes.txt") as file:
        contents = file.read()
        quote = random.choice(contents.splitlines())

    with smtplib.SMTP("smtp.mail.yahoo.com", port=587) as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="gizat.makhanov@gmail.com",
            msg=f"Subject:Quote of the day\n\n{quote}")
