#!/usr/bin/env python

"""Tests for `day_003` package."""

from src.days_of_code import day_003 as d
import pytest


@pytest.fixture
def scenes():
    game = d.Game()
    yield game.scenes


def test_json(scenes):
    assert scenes["s1"]["choices"][0]["choice"] == "left"


# def test_scenario_1a1(monkeypatch):
#     inputs = iter(["right"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     game = d.Game()
#     result = game.play()
#     assert result == "Fall into a hole.\nGame over."


def individual_scenario_test(scenes, scene_key, input_list, expectation):
    monkeypatch = pytest.MonkeyPatch()
    inputs = iter(input_list)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    scene = scenes[scene_key]
    game = d.Game()
    result = game.scenario(scene)
    assert result is expectation


def test_scenario1(scenes):
    individual_scenario_test(scenes, "s1", ["left"], True)
    individual_scenario_test(scenes, "s1", ["right"], False)
    individual_scenario_test(scenes, "s1", ["foo"], False)


def test_scenario2(scenes):
    individual_scenario_test(scenes, "s2", ["wait"], True)
    individual_scenario_test(scenes, "s2", ["swim"], False)
    individual_scenario_test(scenes, "s2", ["foo"], False)


def test_scenario3(scenes):
    individual_scenario_test(scenes, "s3", ["yellow"], True)
    individual_scenario_test(scenes, "s3", ["red"], False)
    individual_scenario_test(scenes, "s3", ["blue"], False)
    individual_scenario_test(scenes, "s3", ["foo"], False)


# def test_scenario_1a(scenes):
#     individual_scenario_test(scenes, "s1", ["left"], True)
#
#
# def test_scenario_1b(monkeypatch, scenes):
#     individual_scenario_test(scenes, "s1", ["right"], False)
#
#
# def test_scenario_1c(monkeypatch, scenes):
#     individual_scenario_test(scenes, "s1", ["foo"], False)


def test_scenario_2a(monkeypatch, scenes):
    inputs = iter(["wait"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    scene = scenes["s2"]
    game = d.Game()
    result = game.scenario(scene)
    assert result is True


def test_scenario_2b(monkeypatch, scenes):
    inputs = iter(["swim"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    scene = scenes["s2"]
    game = d.Game()
    result = game.scenario(scene)
    assert result is False


def test_scenario_2c(monkeypatch, scenes):
    inputs = iter(["foo"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    scene = scenes["s2"]
    game = d.Game()
    result = game.scenario(scene)
    assert result is False


# def test_scenario_2a1(monkeypatch):
#     inputs = iter(["left", "swim"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     game = d.Game()
#     result = game.play()
#     assert result == "Attacked by trout.\nGame over."


# def test_scenario_2a2(monkeypatch):
#     inputs = iter(["left", "foo"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     game = d.Game()
#     result = game.play()
#     assert result == "Attacked by trout.\nGame over."


# def test_scenario_3a(monkeypatch):
#     inputs = iter(["left", "wait", "red"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     game = d.Game()
#     result = game.play()
#     assert result == "Burned by fire.\nGame over."
#
#
# def test_scenario_3b(monkeypatch):
#     inputs = iter(["left", "wait", "blue"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     game = d.Game()
#     result = game.play()
#     assert result == "Eaten by beasts.\nGame over."
#
#
# def test_scenario_3c(monkeypatch):
#     inputs = iter(["left", "wait", "foo"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     game = d.Game()
#     result = game.play()
#     assert result == "Game over."
#
#
# def test_scenario_3d(monkeypatch):
#     inputs = iter(["left", "wait", "yellow"])
#     monkeypatch.setattr("builtins.input", lambda _: next(inputs))
#     game = d.Game()
#     result = game.play()
#     assert result == "You win!"
