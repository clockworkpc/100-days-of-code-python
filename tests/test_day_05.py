#!/usr/bin/env python

"""Tests for `day_05` package."""

from src.days_of_code import day_05 as d
import pytest
import json
import os
import re


@pytest.fixture
def my_chars():
    json_ary = "tests/assets/password_characters.json".split("/")
    json_path = os.path.join(os.getcwd(), *json_ary)
    return json.load(open(json_path, "r"))


@pytest.fixture
def g():
    yield d.Generator()


def test_characters(my_chars):
    g = d.Generator()
    assert g.characters["letters"] == my_chars["letters"]
    assert g.characters["numbers"] == my_chars["numbers"]
    assert g.characters["symbols"] == my_chars["symbols"]


def test_get_inputs(g):
    monkeypatch = pytest.MonkeyPatch()
    inputs = iter(["5", "4", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = g.get_inputs()
    assert result == {"letters": 5, "numbers": 4, "symbols": 3}


def password_check(my_inputs, res_str):
    letters = re.findall("[a-zA-Z]", res_str)
    assert len(letters) == my_inputs["letters"]
    numbers = re.findall("[0-9]", res_str)
    assert len(numbers) == my_inputs["numbers"]
    symbols = re.findall("[!#$%&()*+]", res_str)
    assert len(symbols) == my_inputs["symbols"]


def test_generate_password(g):
    my_inputs = {"letters": 5, "numbers": 4, "symbols": 3}
    res = g.generate_password_list(my_inputs)
    res_str = "".join(res)
    password_check(my_inputs, res_str)


def test_main(g):
    monkeypatch = pytest.MonkeyPatch()
    my_inputs = {"letters": 5, "numbers": 4, "symbols": 3}
    inputs = iter(["5", "4", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    res_str = g.main()
    password_check(my_inputs, res_str)
