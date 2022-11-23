# _______________________ Imports ___________________
import smtplib
import random
import datetime as dt

# _____________________ User information__________

sender_email = "hank77981@gmail.com"
password = "pvpsjvhslpoagkpk"

# _____________________ handling with file__________

# TODO: open and save the file in local variable and convert into list
with open("quotes.txt") as file:
    data = file.read()
    quote_list = data.split("\n")

# TODO: choose random quote from the list of quotes
choose_quote = random.choice(quote_list)

# TODO: Find out the current day
current_date = dt.datetime.now()
current_weekday = current_date.weekday()


# TODO: If it is monday send the mail
if current_weekday == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(from_addr=sender_email, to_addrs="mohdahmedk@gmail.com",
                            msg=f"Subject: Monday motivation \n\n {choose_quote}\n\nHave a nice week.\n-hanK")



