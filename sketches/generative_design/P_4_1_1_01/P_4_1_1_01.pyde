# P_4_1_1_01
 
import datetime
 

def setup():
    global img, img_tiles, tile_count_x, tile_count_y, tile_width, tile_height, select_mode, random_mode
    
    size(1600, 1200)
    img = loadImage('data/img.jpg')
    img_tiles = []
    tile_count_x = 4
    tile_count_y = 4
    tile_width = width / tile_count_x
    tile_height = height / tile_count_y
    noFill()
    stroke(255)
    noCursor()
    select_mode = True
    random_mode = False
    
    
def draw():
    global crop_x, crop_y
    
    if select_mode:
        crop_x = constrain(mouseX, 0, width - tile_width)
        crop_y = constrain(mouseY, 0, height - tile_height)
        image(img, 0, 0)
        rect(crop_x, crop_y, tile_width, tile_height)
    else:
        i = 0
        for y in range(tile_count_y):
            for x in range(tile_count_x):
                image(img_tiles[i], x * tile_width, y * tile_height)
                i += 1
                
                
def crop_tiles():
    global tile_width, tile_height, tile_count, img_tiles, crop_x, crop_y
    
    tile_width = width / tile_count_x
    tile_height = height / tile_count_y
    tile_count = tile_count_x * tile_count_y
    img_tiles = []
    
    for y in range(tile_count_y):
        for x in range(tile_count_x):
            if random_mode:
                crop_x = int(random(mouseX - tile_width / 2, mouseX + tile_width / 2))
                crop_y = int(random(mouseY - tile_height / 2, mouseY + tile_height / 2))
    
            crop_x = constrain(mouseX, 0, width - tile_width)
            crop_y = constrain(mouseY, 0, height - tile_height)
            img_tiles.append(img.get(crop_x, crop_y, tile_width, tile_height))
    
    
def mouseMoved():
    global select_mode
    select_mode = True
    

def mouseReleased():
    global select_mode
    select_mode = False
    crop_tiles()
    

def keyReleased():
    global tile_count_x, tile_count_y
    
    if ((key == 's') or (key == 'S')):
        saveFrame('{}.png'.format(datetime.datetime.now()))  
    if key == 'r' or key == 'R':
        random_mode = !random_mode
    if key == '1':
        tile_count_x = 4
        tile_count_y = 4
        crop_tiles()
    if key == '2':
        tile_count_x = 10
        tile_count_y = 10
        crop_tiles()
    if key == '3':
        tile_count_x = 20
        tile_count_y = 20
        crop_tiles()
    
