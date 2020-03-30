from pynput.mouse import Button, Controller
import time
import keyboard  # using module keyboard

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))
print('Press \'q\' to exit program')

while True:  # making a loop

    # Set pointer position
    mouse.position = (500, 500)

    time.sleep(0.5)

	# Set pointer position
    mouse.position = (600, 600)

    time.sleep(0.5)

    if keyboard.is_pressed('q'):  # if key 'q' is pressed 
        print('Exiting program')
        break

print('Program Finished')
