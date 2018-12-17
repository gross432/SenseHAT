from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()
sense.clear()
game_over = False
x = 0
y = 0
r = (255, 0, 0)
b = (0, 0, 255)
g = (0, 255, 0)
a = (192, 192, 192)
e = (0, 0, 0)
    

maze1 = [[a,e,b,b,r,b,b,b],
        [b,e,e,e,e,e,e,b],
        [b,b,b,b,e,b,r,b],
        [b,b,b,b,e,b,r,b],
        [b,e,e,e,e,e,e,b],
        [b,e,b,b,e,b,b,b],
        [b,e,b,r,e,e,b,b],
        [b,g,b,b,b,b,b,b]]
maze2 = [[b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b]]
maze3 = [[b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b],
        [b,b,b,b,b,b,b,b]]
maze4 = [[a,e,b,b,b,b,b,b],
        [b,e,b,e,e,e,r,b],
        [b,e,r,e,r,e,r,b],
        [b,e,e,e,e,e,e,b],
        [b,e,r,e,r,e,g,b],
        [b,e,e,e,e,e,r,b],
        [b,b,e,b,b,b,b,b],
        [b,b,b,b,b,b,b,b]]
maze5 = [[b,g,b,b,r,b,b,b],
        [b,e,e,e,e,e,e,b],
        [b,b,b,b,e,b,r,b],
        [b,b,b,b,e,b,r,b],
        [b,e,e,e,e,e,e,b],
        [b,e,b,b,e,b,b,b],
        [b,a,b,r,e,e,b,b],
        [b,b,b,b,b,b,b,b]]
mazes = [maze1, maze2, maze3, maze4, maze5]
maze = random.choice(mazes)
def check_wall(x, y, new_x, new_y):
    if maze[new_y][new_x] != b:
        return new_x, new_y
    elif maze[new_y][x] != b:
        return x, new_y
    elif maze[y][new_x] !=  b:
        return new_x, y
    else:
        return x,y
    
def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 10 < pitch < 170 and x != 0:
        new_x -= 1
    if 190 < pitch < 350 and x != 7:
        new_x += 1
    if 190 < roll < 350 and y != 0:
        new_y -= 1
    if 10 < roll < 170 and y != 7:
        new_y += 1
    new_x, new_y = check_wall(x,y,new_x,new_y)
    return new_x, new_y
    
    
while game_over == False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x,y = move_marble(pitch, roll, x, y)
    
    maze[y][x] = a
    sense.set_pixels(sum(maze,[]))
    sleep(0.1)
    maze[y][x] = e
