from cell import Cell
from cell_controller import CellController


def setup():
    size(800, 800)
    background(255)
    init()
    
    
def draw():
    background(255)
    controller.update()
    controller.render()
    
    # noLoop()
    saveFrame('frames/######.png')
    
    
def init():
    global controller
    
    dirs = ['north', 'east', 'south', 'west']
    controller = CellController(dirs)
    cell = Cell(50, 50, 40, 20, dirs[1])
    controller.add_cell(cell)
    
def keyPressed():
    filename = 'images/eddifice_{}{}{}.png'.format(minute(), second(), millis())
    if key == 's':
        save(filename)
