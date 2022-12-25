# P_2_2_3_01
import datetime


x = 0
y = 0
step_size = 5.0

font = 'Georgia'
# letters = 'The Times 03/Jan/2009 Chancellor on brink of second bailout for banks'
letters = 'Young Dumb and Broke'
font_size_min = 3
angle_distortion = 0.0

counter = 0


def setup():
    global x, y, font
    
    size(1000, 1000)
    background(255)
    smooth()
    cursor(CROSS)
    
    x = mouseX
    y = mouseY
    
    font = createFont('American Typewriter', 10)
    textFont(font, font_size_min)
    fill(0)
    

def draw():
    global x, y, counter
    
    if mousePressed:
        d = dist(x, y, mouseX, mouseY)
        textFont(font, font_size_min + (d / 2))
        new_letter = letters[counter]
        step_size = textWidth(new_letter)
        
        if d > step_size:
            # print('d = ', d, ' | step size = ', step_size)
            # print('(x:{}, y:{})'.format(x, y))
            # print('(mouseX:{}, mouseY:{})'.format(mouseX, mouseY))
            # print('counter: ', counter, ' new letter: ', new_letter)
            
            angle = atan2(mouseY - y, mouseX - x)
            
            push()
            translate(x, y)
            rotate(angle + random(angle_distortion))
            text(new_letter, 0, 0)
            pop()
            
            counter += 1
            if counter >= len(letters):
                counter = 0
                
            x = x + cos(angle) * step_size
            y = y + sin(angle) * step_size
            
            
def mousePressed():
    x = mouseX
    y = mouseY
    
            
            
def keyReleased():
    if ((key == DELETE) or (key == BACKSPACE)):
        background(255)
    if ((key == 's') or (key == 'S')):
        saveFrame('{}.png'.format(datetime.datetime.now()))            
            
            
def keyPressed():
    global angle_distortion
    
    if keyCode == UP:
        angle_distortion += 0.1            
    if keyCode == DOWN:
        angle_distortion -= 0.1
