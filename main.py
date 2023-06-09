
import pandas
import datetime as dt
import random
import smtplib

birthdays = pandas.read_csv('birthdays.csv')
birthdays = birthdays.to_dict(orient='records')

email = ''
password = ''
now = dt.datetime.now()

for info in birthdays:
    birthday = dt.datetime(info['year'], info['month'], info['day'])
    if birthday.month == now.month and birthday.day == now.day:
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as file:
            birthday_wish = file.readlines()

        birthday_wish = ''.join(birthday_wish)
        birthday_wish = birthday_wish.replace('[NAME]', '{info["name"]}')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=info['email'],
                                msg='Subject: Happy Birthday\n\n'f'{birthday_wish}')
