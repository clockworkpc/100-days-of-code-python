def turn_right():
    for _ in range(3):
        turn_left()


def left_is_clear():
    turn_left()
    check = wall_in_front()
    turn_right()
    return check


running = True
while running:
    if at_goal():
        running = False
        break

    go = True
    while go:
        if at_goal():
            running = False
            break

        if front_is_clear():
            if right_is_clear():
                turn_right()
                move()
            else:
                move()
        else:
            go = False

    if wall_in_front():
        if right_is_clear():
            if at_goal():
                running = False
                break
            turn_right()
            move()
        if wall_on_right():
            turn_left()
