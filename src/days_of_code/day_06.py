"""Day 6: Reeborg's World"""

import json


class Reeborg:
    """docstring for Reeborg."""

    def __init__(self, world_path, position=None, direction=None):
        super(Reeborg, self).__init__()
        self.world = json.load(open(world_path, "r"))
        self.position = position or {"x": 1, "y": 1}
        self.direction = direction or "north"
        self.x = self.position["x"]
        self.y = self.position["y"]

    def coordinates(self):
        return ",".join(map(str, self.position.values()))

    def at_world_edge(self):
        return self.x in [1, self.world["cols"]] or self.position["y"] in [
            1,
            self.world["rows"],
        ]

    def is_adjacent_wall(self):
        return self.at_world_edge() or self.coordinates() in self.world["walls"].keys()

    def wall_in_front(self):
        def facing_world_edge():
            facing_south = self.y == 1 and self.direction == "south"
            facing_north = self.y == 6 and self.direction == "north"
            facing_east = self.x == 6 and self.direction == "east"
            facing_west = self.x == 1 and self.direction == "west"

            return facing_south or facing_north or facing_east or facing_west

        return (
            facing_world_edge()
            or self.direction in self.world["walls"][self.coordinates()]
        )

    def move(self):
        move_actions = {
            "east": lambda: self.position.update({"x": self.x + 1}),
            "north": lambda: self.position.update({"y": self.y + 1}),
            "west": lambda: self.position.update({"x": self.x - 1}),
            "south": lambda: self.position.update({"y": self.y - 1}),
        }

        if self.is_adjacent_wall() and self.wall_in_front():
            print(f"Cannot move {self.direction}, facing a wall.")
        else:
            action = move_actions.get(self.direction)
            action()

        return self.position

    def turn_left(self):
        turn_actions = {
            "north": lambda: setattr(self, "direction", "west"),
            "west": lambda: setattr(self, "direction", "south"),
            "south": lambda: setattr(self, "direction", "east"),
            "east": lambda: setattr(self, "direction", "north"),
        }

        action = turn_actions.get(self.direction)
        action()

        return self.position

    def front_is_clear(self):
        return not self.wall_in_front()

    def right_is_clear(self):
        right_coordinates = {
            "north": [self.x + 1, self.y],
            "east": [self.x, self.y - 1],
            "south": [self.x - 1, self.y],
            "west": [self.x, self.x],
        }


# def turn_left():
#     print("Turn left")
#
#
# def front_is_clear():
#     print("Front is clear")
#
#
# def right_is_clear():
#     print("right is clear")
#
#
# def at_goal():
#     print("At goal")
#
#
# def move():
#     print("move")
#
#
# # Solution
#
#
# def turn_right():
#     for _ in range(3):
#         turn_left()
#
#
# def left_is_clear():
#     turn_left()
#     if front_is_clear():
#         turn_right()
#         return True
#     if not front_is_clear():
#         turn_right()
#         return False
#
#
# running = True
# while running:
#     if at_goal():
#         running = False
#         break
#
#     if not front_is_clear() and not right_is_clear():
#         turn_left()
#
#     if not front_is_clear() and right_is_clear():
#         turn_right()
#         move()
#
#     if front_is_clear() and right_is_clear():
#         turn_right()
#
#     if front_is_clear():
#         move()
