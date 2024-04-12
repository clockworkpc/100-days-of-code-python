#!/usr/bin/env python

"""Tests for `day_002` package."""

import pytest
from src.days_of_code import day_002 as d


def test_total_plus_tip():
    total_int = 100.00
    tip_int1 = 10
    tip_int2 = 12
    tip_int3 = 15

    res1 = d.total_plus_tip(total_int, tip_int1)
    res2 = d.total_plus_tip(total_int, tip_int2)
    res3 = d.total_plus_tip(total_int, tip_int3)

    assert res1 == 110.00
    assert res2 == 112.00
    assert res3 == 115.00


def test_split_total_plus_tip():
    total_int = 100.00
    guests_int = 5

    tip_int1 = 10
    tip_int2 = 12
    tip_int3 = 15

    res1 = d.split_total_plus_tip(total_int, tip_int1, guests_int)
    res2 = d.split_total_plus_tip(total_int, tip_int2, guests_int)
    res3 = d.split_total_plus_tip(total_int, tip_int3, guests_int)

    assert res1 == 22.00
    assert res2 == 22.40
    assert res3 == 23.00


def test_total_bill_calculator(monkeypatch):
    inputs = iter([124.54, 12, 5])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = d.main()
    assert result == "Each person should pay $27.90"
