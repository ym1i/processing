from random import randint


class Palette():
    def __init__(self):
        self.colors = []
        self.white = color(255, 255, 255)
        self.grey = color(128, 128, 128)
        self.red = color(255, 0, 0)
        self.green = color(0, 255, 0)
        self.blue = color(0, 0, 255)
        
        self.favarite = ['gift_card', 'atlas', 'lux', 'untitled_1', 'untitled_2', 'untitled_4', 'sprague', 'mural', 'docks', 'verena', 'mantis', 'night_life', 'politique', 
                         'lucky_strike', 'tropico']
        
        self.palettes = ['lux', 'black', 'baked', 'politique', 'rad', 'hotspot', 'atlas', 'hotshot', 'my_sore', 'verena', 'gift_card', 
                          'revolution', 'main_course', 'docks', 'mural', 'sprague', 'mantis', 'night_life', 'punk', 'slapdash', 'tropico', 'spider_king', 'mantel_colors',
                         'explosion', 'alt_1', 'alt_3', 'montreux', 'lucky_strike', 'untitled_4', 'untitled_3', 'untitled_2', 'untitled_1']
        
        # self.palettes = ['lux', 'black', 'baked', 'politique', 'rad', 'hotspot', 'atlas', 'hotshot', 'red_spider', 'my_sore', 'yellow_spider', 'verena', 'gift_card', 'blue_spider', 'green_spider',
        #                   'revolution', 'pink_spider', 'main_course', 'docks', 'mural', 'sprague', 'mantis', 'night_life', 'punk', 'slapdash', 'tropico', 'spider_king', 'mono', 'mantel_colors',
        #                   'girl_1', 'girl_2', 'explosion', 'alt_1', 'alt_2', 'alt_3', 'happy', 'montreux', 'lucky_strike', 'untitled_4', 'untitled_3', 'untitled_2', 'untitled_1']
        
        self.kieth_haring = ['montreux', 'lucky_strike', 'untitled_4', 'untitled_3', 'untitled_2', 'untitled_1']
        
        self.select_palette(self.palettes[randint(0, len(self.palettes) - 1)])
        # self.keith(self.kieth_haring[randint(0, len(self.kieth_haring) - 1)])
        
    def random_color(self):
        return self.colors[int(random(len(self.colors)))]    
    
    
    # Kieth Haring
    def montreux(self):
        self.colors = [color(255, 0, 115), color(0, 149, 187), color(255, 109, 0), color(254, 255, 0), color(0, 0, 0)]
        
    def lucky_strike(self):
        self.colors = [color(0, 164, 255), color(255, 0, 0), color(255, 125, 0), color(0, 0, 0), color(255, 255, 255)]
    
    def untitled_1(self):
        self.colors = [color(28, 223, 0), color(255, 0, 0), color(255, 252, 0), color(255, 154, 0), color(0, 0, 0), color(255, 0, 121)]
        
    def untitled_2(self):
        self.colors = [color(255, 252, 0), color(0, 204, 0), color(255, 0, 88), color(255, 0, 0), color(255, 153, 0), color(0, 0, 0)]
    
    def untitled_3(self):
        self.colors = [color(255, 150, 0), color(0, 138, 159), color(97, 238, 254), color(255, 109, 228), color(255, 0, 0), color(255, 149, 0), color(253, 253, 0), color(186, 143, 232),
                       color(0, 179, 0), color(255, 221, 198), color(0, 0, 0), color(255, 255, 255)]
    
    def untitled_4(self):
        self.colors = [color(255, 0, 0), color(255, 255, 0), color(255, 43, 105), color(121, 215, 255), color(58, 158, 0), color(0, 0, 0)]
    
    
    # Fidenza
    def lux(self):
        self.colors = [color(88, 61, 43), color(225, 214, 194), color(255, 184, 0), color(255, 207, 77), color(236, 63, 79), color(255, 172, 156), color(0, 168, 143), color(173, 217, 205),
                       color(26, 96, 142), color(111, 170, 194), color(16, 25, 53), color(245, 118, 14)]
    
    def black(self):
        self.colors = [color(25, 25, 25), color(235, 228, 215)]
        
    def baked(self):
        self.colors = [color(9, 141, 61), color(252, 208, 200), color(103, 75, 55), color(194, 230, 202), color(255, 172, 156), color(248, 247, 243)]
        
    def politique(self):
        self.colors = [color(189, 217, 231), color(26, 96, 142), color(255, 207, 77), color(236, 63, 79), color(255, 172, 156), color(248, 247, 243)]
    
    def rad(self):
        self.colors = [color(225, 214, 194), color(88, 61, 43), color(236, 63, 79), color(228, 0, 35), color(246, 117, 15), color(255, 185, 0), color(111, 170, 194), color(173, 217, 205)]    
                
        
    # Ode To Roy
    def girl_1(self):
        self.colors = [color(241, 229, 159), color(145, 18, 37), color(0, 0, 0)]
        
    def girl_2(self):
        self.colors = [color(251, 222, 0), color(240, 228, 158), color(144, 18, 37), color(0, 42, 118), color(48, 38, 32), color(0, 0, 0), color(255, 255, 255)]
        
    def explosion(self):
        self.colors = [color(250, 0, 0), color(66, 47, 135), color(248, 213, 0), color(249, 230, 123), color(255, 255, 255)]
        
    def alt_1(self):
        self.colors = [color(187, 86, 183), color(0, 135, 250), color(0, 178, 247), color(59, 210, 252), color(0, 0, 0), color(255, 255, 255)]
        
    def alt_2(self):
        self.colors = [color(247, 215, 0), color(250, 231, 124), color(250, 0, 0), color(150, 3, 6), color(0, 0, 0), color(255, 255, 255)]
        
    def alt_3(self):
        self.colors = [color(0, 156, 245), color(153, 153, 226), color(255, 0, 58), color(0, 94, 147), color(0, 0, 0)]
        
    def happy(self):
        self.colors = [color(112, 112, 112), color(195, 123, 119), color(151, 27, 21), color(255,184,0), color(255, 88, 0), color(255, 255, 255)]
    
    # Archetype
    def hotspot(self):
        self.colors = [color(92, 194, 192), color(36, 159, 185), color(246, 244, 202), color(247, 183, 0), color(254,71,0)]
        
    def atlas(self):
        self.colors = [color(36, 159, 57), color(248, 192, 0), color(240, 40, 43), color(245, 232, 210), color(55, 140, 158)] 
        
    def hotshot(self):
        self.colors = [color(229, 231, 208), color(254, 67, 0), color(254, 67, 0), color(149, 187, 193), color(247, 243, 222)]
    
    def red_spider(self):
        self.colors = [color(254, 32, 64), color(246,216,183)]
        
    def my_sore(self):
        self.colors = [color(103, 57, 85), color(242, 168, 61), color(80, 155, 159), color(253, 97, 0)]
   
    def yellow_spider(self):
        self.colors = [color(254, 174, 0), color(246,216,183)]       
        
    def verena(self):
        self.colors = [color(0, 107, 228), color(224, 229, 232), color(255, 73, 65), color(255, 175, 0), color(0, 163, 88), color(142,93,167)]
        
    def gift_card(self):
        self.colors = [color(39, 47, 61), color(60, 99, 209), color(251, 244, 231), color(255, 184, 0), color(255, 59, 67), color(72, 194, 123), color(136, 216, 202), color(0, 140, 165),
                       color(246, 241, 227)]
   
    def blue_spider(self):
        self.colors = [color(0, 123, 159), color(245, 215, 182)]        
        
    def green_spider(self):
        self.colors = [color(0,106,71), color(246,216,183)]
    
    def revolution(self):
        self.colors = [color(0,185,148), color(255,251,194), color(129,85,113), color(248,155,0), color(255,69,86)]
        
    
    def pink_spider(self):
        self.colors = [color(253,121,122), color(246,216,183)]
    
    def main_course(self):
        self.colors = [color(149,71,68), color(255,176,136), color(255,86,75), color(200,124,145), color(211,238,203)]
        
    
    def docks(self):
        self.colors = [color(7,43,55), color(248,195,84), color(112,38,52), color(112,166,190), color(0,132,100), color(226,61,2), color(112,166,190), color(226,61,2), color(238,225,173)]
    
    def mural(self):
        self.colors = [color(233,182,187), color(220,18,14), color(0,128,47), color(38,148,163), color(238,172,0), color(227,221,214)]
        
    def sprague(self):
        self.colors = [color(255,0,17), color(0,152,190), color(255,202,0), color(254,237,220), color(255,163,177), color(0,152,190)]
    
    def mantis(self):
        self.colors = [color(236,176,169), color(218,0,26), color(243,141,0), color(0,136,148), color(0,103,36), color(233,214,169)]
        
    def night_life(self):
        self.colors = [color(0,177,128), color(185,89,159), color(253,136,161), color(255,101,68), color(255,188,26), color(242,231,182), color(0,203,239)]
    
    def punk(self):
        self.colors = [color(254,88,42), color(249,205,0), color(247,243,222)]
    
    def slapdash(self):
        self.colors = [color(251,91,47), color(255,201,0), color(108,168,144), color(251,183,200), color(118,177,218), color(244,245,240)]
    
    def tropico(self):
        self.colors = [color(0,120,36), color(237,213,198), color(229,176,0), color(225,29,0), color(221,106,0), color(87,158,139)]
    
    def spider_king(self):
        self.colors = [color(242, 219, 188), color(230, 63, 71), color(237, 129, 126), color(1, 121, 156), color(0, 103, 73)]
        
    
    def mono(self):
        self.colors.extend([color(217, 63, 29), color(227, 147, 124), color(230, 204, 167)])
            
    
    def golid_colors(self):
        self.colors.extend([color(231, 94, 96), color(249, 190, 82), color(89,180,180), color(197,149,197)])
    
    
    def mantel_colors(self):
        self.colors.extend([color(216, 29, 3), color(16, 25, 157), color(28, 126, 79), color(246, 165, 2), color(239, 212, 191), color(226, 224, 239), color(5, 4, 0)])
        
        
    def keith(self, palette):
        print 'Palette (Keith): ', palette  
        if palette == 'montreux':
            self.montreux()
        elif palette == 'lucky_strike':
            self.lucky_strike()
        elif palette == 'untitled_1':
            self.untitled_1()
        elif palette == 'untitled_2':
            self.untitled_2()
        elif palette == 'untitled_3':
            self.untitled_3()
        elif palette == 'untitled_4':
            self.untitled_4()
    
    
    def select_palette(self, palette):
        self.name = palette
        print 'Palette: ', palette   
        if palette == 'lux':
            self.lux()
        elif palette == 'black':
            self.black()
        elif palette == 'baked':
            self.baked()
        elif palette == 'politique':
            self.politique()
        elif palette == 'rad':
            self.rad()
        elif palette == 'hotspot':
            self.hotspot()
        elif palette == 'atlas':
            self.atlas()
        elif palette == 'hotshot':
            self.hotshot()
        elif palette == 'red_spider':
            self.red_spider()
        elif palette == 'my_sore':
            self.my_sore()
        elif palette == 'yellow_spider':
            self.yellow_spider()
        elif palette == 'verena':
            self.verena()
        elif palette == 'gift_card':
            self.gift_card()
        elif palette == 'blue_spider':
            self.blue_spider()
        elif palette == 'green_spider':
            self.green_spider()
        elif palette == 'revolution':
            self.revolution()
        elif palette == 'pink_spider':
            self.pink_spider()
        elif palette == 'main_course':
            self.main_course()
        elif palette == 'docks':
            self.docks()
        elif palette == 'mural':
            self.mural()
        elif palette == 'sprague':
            self.sprague()
        elif palette == 'mantis':
            self.mantis()
        elif palette == 'night_life':
            self.night_life()
        elif palette == 'punk':
            self.punk()
        elif palette == 'slapdash':
            self.slapdash()
        elif palette == 'tropico':
            self.tropico()
        elif palette == 'spider_king':
            self.spider_king()
        elif palette == 'mono':
            self.mono()
        elif palette == 'mantel_colors':
            self.mantel_colors()
        elif palette == 'girl_1':
            self.girl_1()
        elif palette == 'girl_2':
            self.girl_2()
        elif palette == 'explosion':
            self.explosion()
        elif palette == 'alt_1':
            self.alt_1()
        elif palette == 'alt_2':
            self.alt_2()
        elif palette == 'alt_3':
            self.alt_3()
        elif palette == 'happy':
            self.happy()
        elif palette == 'montreux':
            self.montreux()
        elif palette == 'lucky_strike':
            self.lucky_strike()
        elif palette == 'untitled_1':
            self.untitled_1()
        elif palette == 'untitled_2':
            self.untitled_2()
        elif palette == 'untitled_3':
            self.untitled_3()
        elif palette == 'untitled_4':
            self.untitled_4()
        
        
        
