import smtplib

my_email = "fryphilip99@yahoo.com"
password = "foalcvfybucuxgrf"

with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="gizat.makhanov@gmail.com", 
        msg="Subject:Hello\n\nThis is the body of the email."
    )