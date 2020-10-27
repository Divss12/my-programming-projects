#UNSOLVED by me

import sys
import random

n = int(sys.argv[1])

drone_pos = [0]*n
drone_speed = [0]*n

while min(drone_speed) == 0:
    k = random.randint(0,n-1)
    drone_speed[k] += 1
    
    for i in range(n):
        drone_pos[i] += drone_speed[i]
        
print(sum(drone_pos)/n)