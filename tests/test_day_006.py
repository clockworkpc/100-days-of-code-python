#!/usr/bin/env python

"""Tests for `day_006` package."""

from src.days_of_code import day_006 as d
import pytest
import json
import os
import re


@pytest.fixture
def world_path():
    json_ary = "tests/assets/reeborg_problem_world.json".split("/")
    path = os.path.join(os.getcwd(), *json_ary)
    yield path
    # game = d.Reeborg(path)
    # yield game


@pytest.fixture
def open_position():
    yield {"x": 4, "y": 3}


# @pytest.mark.filter
def test_move_east(world_path, open_position):
    g = d.Reeborg(world_path, open_position, "east")
    g.move()
    assert g.position == {"x": 4 + 1, "y": 3}


def test_move_north(world_path, open_position):
    g = d.Reeborg(world_path, open_position, "north")
    g.move()
    assert g.position == {"x": 4, "y": 3 + 1}


def test_move_west(world_path, open_position):
    g = d.Reeborg(world_path, open_position, "west")
    g.move()
    assert g.position == {"x": 4 - 1, "y": 3}


def test_move_south(world_path, open_position):
    g = d.Reeborg(world_path, open_position, "south")
    g.move()
    assert g.position == {"x": 4, "y": 3 - 1}


def test_move_wall_east(world_path):
    g = d.Reeborg(world_path, None, "east")
    g.move()
    assert g.position == {"x": 1, "y": 1}


def test_move_wall_south(world_path):
    g = d.Reeborg(world_path, None, "south")
    g.move()
    assert g.position == {"x": 1, "y": 1}


def test_move_wall_west(world_path):
    g = d.Reeborg(world_path, None, "west")
    g.move()
    assert g.position == {"x": 1, "y": 1}


# def test_turn_left(world_path):
#     g = d.Reeborg(world_path, None, "north")
#     g.turn_left()
#     assert g.direction == "west"
#     g.turn_left()
#     assert g.direction == "south"
#     g.turn_left()
#     assert g.direction == "east"
#     g.turn_left()
#     assert g.direction == "north"
