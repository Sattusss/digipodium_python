import pgzrun
HEIGHT = 500
WIDTH = 600

box4 = Rect((40,40),(50,50))
def draw():
    screen.fill('Black') 
    screen.draw.filled_rect(box4,'White')
def update():
    control_player()
    if box4.x > WIDTH:
        box4.x = 0
    if box4.x < 0:
        box4.x = WIDTH
    if box4.y > HEIGHT:
        box4.y = 0
    if box4.y < 0:
        box4.y = HEIGHT
    
 

def control_player():
    if keyboard.RIGHT:
        box4.x += 2
    if keyboard.LEFT:
        box4.x -= 2
    #move up and down with y axis
    if keyboard.UP:
        box4.y -= 2
    if keyboard.DOWN:
        box4.y += 2
    
pgzrun.go()