from sense_hat import SenseHat
from time import sleep
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
    

maze1 = [[b,g,b,b,r,b,b,b],
        [b,e,e,e,e,e,e,b],
        [b,b,b,b,e,b,r,b],
        [b,b,b,b,e,b,r,b],
        [b,e,e,e,e,e,e,b],
        [b,e,b,b,e,b,b,b],
        [b,e,b,r,e,e,b,b],
        [b,e,b,b,b,b,b,b]]
def check_wall(x, y, new_x, new_y):
    if maze1[new_x][new_y] != b:
        return new_x, new_y
    elif maze1[new_y][x] != b:
        return x, new_y
    elif maze1[y][new_x]:
        return new_x, y
    else:
        return x,y
def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch < 179 and x != 0:
        new_x -= 1
    if 181 < pitch < 359 and x != 7:
        new_x += 1
    if 181 < roll < 359 and y != 0:
        new_y -= 1
    if 1 < roll < 179 and y != 7:
        new_y += 1
    new_x, new_y = check_wall(x,y,new_x,new_y)
    return new_x, new_y

    
while game_over == False:
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    x,y = move_marble(pitch, roll, x, y)
    
    maze1[y][x] = a
    sense.set_pixels(sum(maze1,[]))
    sleep(0.15)
    maze1[y][x] = e
