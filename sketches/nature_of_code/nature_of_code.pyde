from mover import Mover
from attractor import Attractor
from friction import Friction
from liquid import Liquid


def setup():
    global mover, liquid, attractor
    
    size(640, 360)
    mover = Mover(0, 0, 0, 0, -0.001, 0.01)
    attractor = Attractor(width / 2, height / 2, 20.0)
    friction = Friction(0.01, 1.0)
    #liquid = Liquid(0, height / 2, width, height / 2, 0.1)
    
    
def draw():
    global mover
    
    background(255)
    # liquid.display()
    
    gravity = PVector(0, 0.1)
    friction = friction.friction(mover.vel)
    # drag = liquid.drag(mover.vel) if liquid.is_inside(mover.loc.x, mover.loc.y) else PVector(0, 0)
    
    mover.apply_force(gravity)
    mover.apply_force(friction)
    # mover.apply_force(drag)
    
    mover.update()
    mover.check_boundary()
    mover.display()
