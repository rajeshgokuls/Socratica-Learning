#Random Walk - Your direction is choosen at random as you go thru the way
#Monte Carlo Simulation this concludes my gamble and amble preamble

import random

print(dir(random))
def random_walk(n):
    x = 0
    y = 0
    for i in range(n):

        step = random.choice(['N', 'S', 'E', 'W']) #to do random steps with four directions
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1

    return (x, y)  #return as tuple

for i in range(25):
    walk = random_walk(10)
    print(walk, "Distance from home =",
          abs(walk[0] + abs(walk[1])))  # sum of absolutes values x and y co-ordinates














