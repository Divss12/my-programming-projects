import time
import random

while True:
    #Imagine that I have magic code here that converts accelerometer/gyroscope data into a number (0,1,2,3) that corresponds to the orientation of the pi
    #This is stored in the variable 'orientation'
    
    rotation = random.randint(0,3) #randomly decides rotation
    sense.set_rotation(90*rotation) #sets the rotation
    sense.set_pixels(whatever, color = green) #display the arrow, green is a tuple with correct (R,G,B)
    
    time.sleep(1) #give the user 1 second to orient the pi
    
    orientation = random.randint(0,3) #rn orientation of the thing is just decided randomly
    
    if orientation == rotation: #user has passed
        continue #game continues
    else:
        sense.set_pixels(whatever, color = red) #display the arrow in red
        break #end the game
    
    