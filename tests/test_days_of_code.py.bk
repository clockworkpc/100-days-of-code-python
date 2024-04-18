#!/usr/bin/env python

"""Tests for `days_of_code` package."""

import pytest
from src.days_of_code import days_of_code as d


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    import requests

    return requests.get("https://github.com/audreyr/cookiecutter-pypackage")


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    from bs4 import BeautifulSoup

    res = BeautifulSoup(response.content, features="lxml").title.string
    assert "GitHub" in res


def test_hello_world():
    name = "Bob"
    res = d.hello_world(name)
    assert res == "Hello, Bob!"


def test_hello_world_with_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "Bob")
    assert d.hello_world_with_input() == "Hello, Bob!"
