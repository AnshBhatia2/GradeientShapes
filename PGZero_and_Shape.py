import pgzrun
import random

WIDTH = 300
HEIGHT = 300

def draw() :
    width = WIDTH
    height = HEIGHT - 200
    r = 255
    g = 0
    b = random.randint(120,255)
    for i in range(20) :
        #adding shape to memory
        shape = Rect((0,0),(width,height))
        shape.center = 150,150
        #drawing shape on screen
        screen.draw.rect(shape,(r,g,b))
        width -= 10
        height += 10
        r -= 10
        g += 10



pgzrun.go()