# from pynput.mouse import Button, Controller # for use of mouse
from pynput.keyboard import Key, Controller # for use of mouse
import time # for use of the current time
import keyboard  # using module keyboard
import random # for random number generation

# the mouse to be jittered
mouse = Controller()
keyboard = Controller()
# time at start of program
start_time = time.time()
# time elapsed since program start
jitter_time = reset_time = 1


# every time this function is called, takes the mouse and jitters it around a bit
def jitterMouse(mouse):
    # for i in range(0, 10):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)

    mouse.position = (600 + x, 600 + y)

# super typer will make the keyboard type a phrase and then delete it
def superTyper(keyoard):
    keyboard.press('H')
    keyboard.release('H')
    keyboard.press('e')
    keyboard.release('e')
    keyboard.press('l')
    keyboard.release('l')
    keyboard.press('l')
    keyboard.release('l')
    keyboard.press('o')
    keyboard.release('o')
    keyboard.press(',')
    keyboard.release(',')
    keyboard.press(' ')
    keyboard.release(' ')
    keyboard.press('W')
    keyboard.release('W')
    keyboard.press('o')
    keyboard.release('o')
    keyboard.press('r')
    keyboard.release('r')
    keyboard.press('l')
    keyboard.release('l')
    keyboard.press('d')
    keyboard.release('d')
    keyboard.press('!')
    keyboard.release('!')



# resets the mouse back to 600, 600. in case it gets too far from the middle
def resetMouse(mouse):
    mouse.position = (600,600)


# Read pointer position
# print('The current pointer position is {0}'.format(mouse.position))
print('Press \'q\' to exit program')

while True:

    # breaking out of while loop is 'q' is pressed
    if keyboard.is_pressed('q'):
        print('Exiting program')
        break

    # couting up in miliseconds
    reset_time = time.time() - start_time
    jitter_time = time.time() - start_time

    # print('jitterRound %d', round(jitter_time) % 2)
    # print('resetRound %d', round(reset_time) % 60)

    # every two seconds, jitter mouse
    if round(jitter_time) % 3 == 0:
        # jitterMouse(mouse)
        superTyper(keyboard)
        jitter_time = 1

    # every 60 seconds, reset mouse to pos 500, 500
    # if round(reset_time) % 60 == 0:
    #     resetMouse(mouse)

print('Program Finished')
