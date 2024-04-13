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


def individual_scenario_test(scenes, scene_key, input_list, expectation):
    monkeypatch = pytest.MonkeyPatch()
    inputs = iter(input_list)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    scene = scenes[scene_key]
    game = d.Game()
    result = game.scenario(scene)
    assert result is expectation


def scenario_sequence_test(scenes, hsh, expectation):
    monkeypatch = pytest.MonkeyPatch()
    input_list = list(hsh.values())
    inputs = iter(input_list)
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    game = d.Game()
    result = game.play()
    assert result == expectation


def test_scenario1(scenes):
    individual_scenario_test(scenes, "s1", ["left"], True)
    individual_scenario_test(scenes, "s1", ["right"], False)
    individual_scenario_test(scenes, "s1", ["foo"], False)


def test_sequence1(scenes):
    message = "Fall into a hole.\nGame over."
    scenario_sequence_test(scenes, {"s1": "right"}, message)
    scenario_sequence_test(scenes, {"s1": "foo"}, message)


def test_scenario2(scenes):
    individual_scenario_test(scenes, "s2", ["wait"], True)
    individual_scenario_test(scenes, "s2", ["swim"], False)
    individual_scenario_test(scenes, "s2", ["foo"], False)


def test_sequence2(scenes):
    message = "Attacked by trout.\nGame over."
    scenario_sequence_test(scenes, {"s1": "left", "s2": "swim"}, message)
    scenario_sequence_test(scenes, {"s1": "left", "s2": "foo"}, message)


def test_scenario3(scenes):
    individual_scenario_test(scenes, "s3", ["yellow"], True)
    individual_scenario_test(scenes, "s3", ["red"], False)
    individual_scenario_test(scenes, "s3", ["blue"], False)
    individual_scenario_test(scenes, "s3", ["foo"], False)


def test_sequence3(scenes):
    sequence3a = {"s1": "left", "s2": "wait", "s3": "red"}
    message1 = "Burned by fire.\nGame over."
    scenario_sequence_test(scenes, sequence3a, message1)

    sequence3b = {"s1": "left", "s2": "wait", "s3": "blue"}
    message2 = "Eaten by beasts.\nGame over."
    scenario_sequence_test(scenes, sequence3b, message2)

    sequence3c = {"s1": "left", "s2": "wait", "s3": "yellow"}
    message3 = "You win!"
    scenario_sequence_test(scenes, sequence3c, message3)

    message4 = "Game over."
    scenario_sequence_test(scenes, {"s1": "left", "s2": "wait", "s3": "foo"}, message4)
