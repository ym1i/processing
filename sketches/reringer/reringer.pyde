from peg import Peg
from wrapper import Wrapper
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    init()
    
    
def draw():
    noLoop()
    render()
    # saveFrame('frames/######.png')


def render():
    for wrapping in wrappings:    
        wrapping.render()
    for peg in pegs:
        peg.render()
    
    
def init():
    global pegs, wrappings, plt, colors
    
    plt = Palette()
    colors = []
    for i in range(100):
        colors.append(plt.random_color())
    
    # MAKE PEGS
    pegs = []
    n_col = 3
    n_row = 3
    margin = 100
    grid_width = (width - margin * 2) / n_col
    grid_height = (height - margin * 2) / n_row
    r = grid_width * 0.2
    
    for j in range(n_row):
        for i in range(n_col):
            loc = PVector(i * grid_width + grid_width * 0.5 + margin, j * grid_height + grid_height * 0.5 + margin)
            pegs.append(Peg(loc=loc, r=r, plt=plt))
    
    # WRAP
    wrappings = []  
    
    # wrap 1            
    id = [0, 1, 2, 5, 8, 7, 4, 3]
    pegs_for_wrapping = []
    for i in id:
        pegs_for_wrapping.append(pegs[i])
    
    wrappings.append(Wrapper(pegs_for_wrapping, plt))  
    
    # wrap 2
    # id = [3, 4, 7, 6]
    # pegs_for_wrapping = []
    # style = 'OUTER'
    # for i in id:
    #     pegs_for_wrapping.append(pegs[i])
    
    # wrappings.append(Wrapper(pegs_for_wrapping, style, plt))        
        
    
def keyPressed():
    filename = 'images/eddifice_{}{}{}.png'.format(minute(), second(), millis())
    if key == 's':
        save(filename)
