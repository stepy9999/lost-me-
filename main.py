"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    I have to write code to make zebra lines
    """
    # define main function
    #put beeper
    #move 
    #put beeper
    #turn left
    #move
    #put beepr
    #move
    #put beeper
    while front_is_clear():
        walk_straight()
        turn_around()

def walk_straight():
    put_two_beepers()

    if front_is_clear():
        move_thrice()
    else:
        turn_around()
    put_two_beepers()
    move_thrice()
    put_two_beepers()
    
def move_thrice():
    if front_is_clear():
       move()
       move()
       move()
       move()
    else:
        turn_around()

def put_two_beepers():
    put_beeper()
    move()
    put_beeper()


    

def turn_around():
    go_back()
    turn_right()
    if front_is_clear():
       move()
       turn_right()
    else:
        turn_right()
        while front_is_clear():
            move()
        while front_is_blocked():
            turn_right()
        while front_is_clear():
            move()
        turn_left()  


def go_back():
    while front_is_blocked():
        turn_left()
        turn_left()
    while front_is_clear():
        move()

def turn_right():
    turn_left()
    turn_left()
    turn_left()





        
        



    


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()