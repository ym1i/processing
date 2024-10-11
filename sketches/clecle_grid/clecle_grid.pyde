from circle import Circle
from connector import Connector
from connector_v import ConnectorV
from connector4 import Connector4
from palette import Palette


def setup():
    size(800, 800)
    background(255)
    init()
    
    
def draw():
    background(255)
    # noLoop()
    for obj in objs:
        obj.update()
    for connector in connectors:
        connector.update()
    render()
    # saveFrame('frames/######.png')


def render():
    for connector in connectors:
        connector.render()
    for obj in objs:
        obj.render()
    
    
def init():
    global objs, connectors
    
    plt = Palette()
    colors = []
    for i in range(100):
        colors.append(plt.random_color())
    
    # Circle Objects in grid layout
    objs = []
    n_col = 4
    n_row = 4
    margin = 100
    grid_width = (width - margin * 2) / n_col
    grid_height = (height - margin * 2) / n_row
    r = grid_width * 0.4
    
    for j in range(n_row):
        for i in range(n_col):
            pos = PVector(i * grid_width + grid_width * 0.5 + margin, j * grid_height + grid_height * 0.5 + margin)
            objs.append(Circle(pos=pos, r=r, plt=plt))
            
    # Connector of the Circle objects
    connectors = []
    
    for j in range(n_row):
        for i in range(n_col - 1):
            id = (j * n_row) + i
            connectors.append(Connector(objs[id], objs[id + 1], plt.random_color(), plt))
    
    for j in range(n_row - 1):
        for i in range(n_col - 1):
            id = (j * n_row) + i
            connectors.append(Connector4(objs[id], objs[id + 1], objs[id + n_col + 1], objs[id + n_col], plt.random_color(), plt))
    
    for j in range(n_row - 1):
        for i in range(n_col):
            id = (j * n_row) + i
            connectors.append(ConnectorV(objs[id], objs[id + n_col], plt.random_color(), plt))
       
    
def keyPressed():
    filename = 'images/clecle_{}{}{}.png'.format(minute(), second(), millis())
    if key == 's':
        save(filename)
