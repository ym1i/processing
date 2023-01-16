# P_4_2_1_01

import datetime


class CollageItem(object):
    def __init__(self, img):
        self.img = img
        self.x = 0
        self.y = 0
        self.rotation = 0
        self.scaling = 1
        

def generate_collage_items(layer_images, count, pos_x, pos_y, range_x, range_y, min_scale, max_scale, min_rotation, max_rotation):
    print('> generate_colage_items()')
    
    collage_items = []
    for i in range(count):
        index = i % len(layer_images)
        item = CollageItem(layer_images[index])
        item.x = pos_x + random(-range_x / 2, range_x / 2)
        item.y = pos_y + random(-range_y / 2, range_y / 2) 
        item.scaling = random(min_scale, max_scale)
        item.rotation = random(min_rotation, max_rotation)
        collage_items.append(item)
        
    return collage_items    


def draw_collage_items(collage_items):
    print('> draw_colage_items()')
    
    for i in range(len(collage_items)):
        item = collage_items[i]
        push()
        translate(item.x, item.y)
        rotate(item.rotation)
        scale(item.scaling)
        image(item.img, 0, 0)
        pop()    
    

def setup():
    print('> setup()')
    
    global layer1_items, layer2_items, layer3_items
    size(1024, 768)
    imageMode(CENTER)
    background(255)
    
    layer1_images = []
    layer2_images = []
    layer3_images = []
    
    for i in range(8):
        layer1_img = 'data/layer_1/sbf_{}.jpg'.format(i)
        layer1_images.append(loadImage(layer1_img))
        layer2_img = 'data/layer_2/cz_{}.jpg'.format(i)
        layer2_images.append(loadImage(layer2_img))
        layer3_img = 'data/layer_3/elon_{}.jpg'.format(i)
        layer3_images.append(loadImage(layer3_img))
    
    layer1_items = generate_collage_items(layer1_images, 100, width / 2, height / 2, width, height, 0.1, 0.5, 0, 0)
    layer2_items = generate_collage_items(layer2_images, 150, width / 2, height / 2, width, height, 0.03, 0.08, -HALF_PI, HALF_PI)
    layer3_items = generate_collage_items(layer3_images, 110, width / 2, height / 2, width, height, 0.01, 0.05, 0, 0)
    
    draw_collage_items(layer1_items)
    draw_collage_items(layer2_items)
    draw_collage_items(layer3_items)    
        

def keyReleased():
    global layer1_items, layer2_items, layer3_items
    
    if key == 's':
        saveFrame('{}.png'.format(datetime.datetime.now()))
    if key == '1': 
        layer1_items = generate_collage_items(layer1_images, random(50, 200), width / 2, height / 2, width, height, 0.1, 0.5, 0, 0)
    if key == '2': 
        layer2_items = generate_collage_items(layer2_images, random(50, 200), width / 2, height / 2, width, height, 0.1, 0.5, 0, 0)
    if key == '3': 
        layer3_items = generate_collage_items(layer3_images, random(50, 200), width / 2, height / 2, width, height, 0.1, 0.5, 0, 0)
        
    clear()

    draw_collage_items(layer1_items)
    draw_collage_items(layer2_items)
    draw_collage_items(layer3_items)
