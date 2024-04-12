#!/usr/bin/env python

"""Tests for `day_003` package."""

from src.days_of_code import day_003 as d


def test_scenario_1a(monkeypatch):
    inputs = iter(["right"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game = d.Game()
    result = game.play()
    assert result == "Fall into a hole.\nGame over."


def test_scenario_2a(monkeypatch):
    inputs = iter(["left", "swim"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game = d.Game()
    result = game.play()
    assert result == "Attacked by trout.\nGame over."


def test_scenario_3a(monkeypatch):
    inputs = iter(["left", "wait", "red"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game = d.Game()
    result = game.play()
    assert result == "Burned by fire.\nGame over."


def test_scenario_3b(monkeypatch):
    inputs = iter(["left", "wait", "blue"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game = d.Game()
    result = game.play()
    assert result == "Eaten by beasts.\nGame over."


def test_scenario_3c(monkeypatch):
    inputs = iter(["left", "wait", "foo"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game = d.Game()
    result = game.play()
    assert result == "Game over."


def test_scenario_3d(monkeypatch):
    inputs = iter(["left", "wait", "yellow"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game = d.Game()
    result = game.play()
    assert result == "You win!"
