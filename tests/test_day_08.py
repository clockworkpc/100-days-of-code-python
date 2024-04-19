#!/usr/bin/env python

"""Tests for `day_08` package."""

from src.days_of_code import day_08 as d
import pytest


@pytest.fixture
def caesar():
    yield d.Caesar()


@pytest.mark.parametrize(
    "char,shift_amount,expected",
    [("a", 9, 9), ("k", 10, 20), ("z", 2, 1), ("z", 26, 25)],
)
def test_new_position(caesar, char, shift_amount, expected):
    assert caesar.shift_position(char, shift_amount) == expected


@pytest.mark.parametrize(
    "start_text,shift_amount,expected",
    [("abc", 1, "bcd"), ("abc", 26, "abc"), ("xyz", 3, "abc"), ("xyz", 26, "xyz")],
)
def test_encode(caesar, start_text, shift_amount, expected):
    assert caesar.encode(start_text, shift_amount) == expected


@pytest.mark.parametrize(
    "start_text,shift_amount,expected",
    [("bcd", 1, "abc"), ("abc", 26, "abc"), ("abc", 3, "xyz"), ("xyz", 26, "xyz")],
)
def test_decode(caesar, start_text, shift_amount, expected):
    assert caesar.decode(start_text, shift_amount) == expected
