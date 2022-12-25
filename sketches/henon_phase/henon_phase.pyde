# HENON PHASE DEEP
# based on the code by J Tarbell and Paul Bourke
# http://www.complexification.net/gallery/machines/henonPhaseDeep/appletl/henonPhaseDeep_l.pde
# ________________________________________________________________________________________________________________________

add_library('controlP5')

from traveler_henon import TravelerHenon
from palette import Palette


def setup():
    global dim, s, a, num, max_num, travelers, pallet, cp5, slider_a, slider_s
    
    cp5 = ControlP5(this)
    slider_a = cp5.addSlider('a').setPosition(10, 10).setSize(200,10).setRange(0.1, PI/ 2).setValue(PI / 4).setNumberOfTickMarks(30)
    slider_s = cp5.addSlider('s').setPosition(10, 30).setSize(200,10).setRange(0.01, 1).setValue(0.73).setNumberOfTickMarks(30)
    
    dim = 500
    s = 0.73
    a = PI / 4
    num = 0
    max_num = 3000
    travelers = []
    pallet = Palette(512)
    pallet.take_colors('pantone.png')
    
    size(500, 500)
    background(255)
    noStroke()
    
    for i in range(max_num):  
        travelers.append(TravelerHenon(s, a, dim, pallet.good_colors, pallet.num_pal))
        num += 1
        
        
def draw():
    global slider_a, slider_s
            
    for k in range(20):
        for i in range(num):
            if frameCount % 50 == 0:
                travelers[i].update_params(slider_a.getValue(), slider_s.getValue())
            travelers[i].draw()
            
    for k in range(2):
        travelers[int(random(num))].create_particle(pallet.good_colors, pallet.num_pal)
    

def mousePressed():
    background(255)
    
    
