#!/usr/bin/python
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
import os
import pandas
import random
import smtplib
import sys


class Emailer:
    def __init__(self):
        sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
        load_dotenv(find_dotenv())
        self.email = os.getenv("MY_EMAIL")
        self.password = os.getenv("MY_PASSWORD")
        self.birthdays = self.get_birthdays()
        self.smtp_server_address = os.getenv("SMTP_SERVER_ADDRESS")

    def get_birthdays(self):
        path = "src/days_of_code/assets/csv/birthdays.csv"
        data = pandas.read_csv(path)

        birthdays_dict: dict[tuple[int, int], any] = {}
        for index, data_row in data.iterrows():
            key: tuple[int, int] = (data_row["month"], data_row["day"])
            birthdays_dict[key] = data_row
        return birthdays_dict

    def get_random_letter_template(self, birthday_person):
        file_path = f"src/days_of_code/assets/txt/letter_{random.randint(1,3)}.txt"

        with open(file_path) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday_person["name"])
        return contents

    def send_mail(self, birthday_person, contents):
        with smtplib.SMTP(self.smtp_server_address) as connection:
            connection.starttls()
            connection.login(self.email, self.password)
            res = connection.sendmail(
                from_addr=self.email,
                to_addrs=birthday_person["email"],
                msg=f"Subject:Happy Birthday!\n\n{contents}",
            )
        return res

    def main(self, key: tuple = None):
        if key is None:
            today = datetime.now()
            key = (today.month, today.day)

        if key in self.birthdays:
            birthday_person = self.birthdays[key]
            contents = self.get_random_letter_template(birthday_person)
            res = self.send_mail(birthday_person, contents)
            return res


#
