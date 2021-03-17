import datetime as dt
from random import choice
import smtplib

my_email = ""
password = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = choice(all_quotes)
    
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="gizat.makhanov@gmail.com", 
            msg=f"Subject:Hello\n\n{quote}"
        )