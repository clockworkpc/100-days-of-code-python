#!/usr/bin/env python

"""Tests for `day_32` package."""

from src.days_of_code import day_32 as d
import pytest


@pytest.fixture
def app():
    yield d.Emailer()


def test_email(app):
    assert app.email == "clockworkpc@gmail.com"


@pytest.mark.parametrize(
    "birthday_info",
    [
        (
            (12, 21),
            {
                "name": "Test",
                "email": "test@email.com",
                "year": 1961,
                "month": 12,
                "day": 21,
            },
        ),
        (
            (1, 31),
            {
                "name": "Foo Bar",
                "email": "foo@bar.com",
                "year": 1990,
                "month": 1,
                "day": 31,
            },
        ),
    ],
)
def test_birthdays(app, birthday_info):
    bday_tuple, expected = birthday_info
    assert app.birthdays[bday_tuple]["name"] == expected["name"]
    assert app.birthdays[bday_tuple]["email"] == expected["email"]
    assert app.birthdays[bday_tuple]["year"] == expected["year"]
    assert app.birthdays[bday_tuple]["month"] == expected["month"]
    assert app.birthdays[bday_tuple]["day"] == expected["day"]


def test_send_email(app):
    key = (5, 20)
    res = app.main(key)
    __import__("ipdb").set_trace()
