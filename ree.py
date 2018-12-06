from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
game_over = False
o = sense.get_orientation()
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
while game_over == False:
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
    maze1[7][1] = a
    sense.set_pixels(sum(maze1,[]))
