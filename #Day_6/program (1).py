#program in reeborg's world
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump_hurdle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
condition = False
while at_goal() != True:
    jump_hurdle()