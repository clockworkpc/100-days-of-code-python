#!/usr/bin/env python

"""Tests for `day_01` package."""

import pytest
from src.days_of_code import day_01 as d


def test_generate_band_name(monkeypatch):
    inputs = iter(["Foo", "Bar"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    result = d.generate_band_name()
    assert result == "Your band name is Foo Bar"
