# HAPPY PLACE
# based on the code by J Tarbell 
# http://www.complexification.net/gallery/machines/happyPlace/index.php
# ________________________________________________________________________________________________________________________

add_library('controlP5')

from friend import Friend
from palette import Palette


def setup():
    global friends, n_friends, dim, time, pallet, max_pal
    friends = []
    dim = 900
    n_friends = 128
    time = 0
    max_pal = 512
    
    # cp5 = ControlP5(this)
    # slider_a = cp5.addSlider('a').setPosition(10, 10).setSize(200,10).setRange(0.1, PI/ 2).setValue(PI / 4).setNumberOfTickMarks(30)
    
    pallet = Palette(512)
    pallet.take_colors('okcomputer.jpg')
    
    size(900, 900)
    background(255)
    frameRate(30)
    
    make_friends()


def draw():
    # Move Friends to HAPPY PLACE
    global time
    
    for i in range(n_friends):
        friends[i].move()
        friends[i].expose()
        friends[i].expose_connections(friends)
        
        if time % 2 == 0:
            friends[i].find_happy_place(friends, n_friends)
    time += 1


def make_friends():
    # Make Friend objects 
    global friends
    
    for i in range(n_friends):
        x = dim / 2 + 0.4 * dim * cos(TWO_PI * i / n_friends)
        y = dim / 2 + 0.4 * dim * sin(TWO_PI * i / n_friends)
        c = pallet.some_color()
        friends.append(Friend(x, y, i, c))
        
    # Make some random Friend connections
    for i in range(n_friends * 2):
        a = floor(random(n_friends))
        b = floor(a + random(22)) % n_friends
        # if b >= n_friends or b < 0:
        #     b = 0
        #     print('b >= num or b < 0')
        if a != b:
            friends[a].connect_to(b)
            friends[b].connect_to(a)
            

def mousePressed():
    background(255)
    make_friends()
