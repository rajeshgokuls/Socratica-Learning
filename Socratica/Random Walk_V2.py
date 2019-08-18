import random
print(dir(random))

def random_walk_2(n):
    """Return coordinates after 'n' block random walk"""
    x,y = 0,0
    for i in range(n):
        (dx,dy) = random.choice([(0,1),(0,-1),(1,0),(-1,0)]) #(N,S,E, W)
        x += dx
        y += dy
    return(x, y)

for i in range(25): # 25 random walks
    walk = random_walk_2(10) #each block would be 10 blocks
    print(walk, "Distance from home=",
          abs(walk[0] + abs(walk[1])))


