#program in reeborg's world
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
        
    while front_is_clear():
        move()
    turn_left()
condition = False
while at_goal() != True:
    if wall_in_front():
        jump_hurdle()
    else:
        move()