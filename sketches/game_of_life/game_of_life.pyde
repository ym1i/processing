from gol import GameOfLife
        
        
def setup():
    global gol
    size(600, 600)
    background(255)
    w = 8
    
    gol = GameOfLife(width / w, height / w, w)


def draw():
    gol.update()
    gol.rebirth()
    gol.render()
    
    
