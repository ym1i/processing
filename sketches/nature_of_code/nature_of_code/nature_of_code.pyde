from particle_system import ParticleSystem
from repeller import Repeller
from attractor import Attractor
from liquid import Liquid
from gravity import Gravity


def setup():
    global ps, repeller, liquid, attractor, friction, gravity
    size(640, 360)
    
    ps = ParticleSystem(PVector(width / 2, 50))
    gravity = Gravity(0.01)
    repeller = Repeller(width / 2, height - 10, 1)
    attractor = Attractor(width / 2, 100)
    liquid = Liquid(0, height / 2, width, height / 10, 0.1)
    
def draw():
    global ps
    background(255)
    
    ps.add_particle()
    
    ps.apply_gravity(gravity)
    ps.apply_repeller(repeller)
    ps.apply_attractor(attractor)
    ps.apply_liquid(liquid)
    
    ps.run()
    ps.check_boundary()
    
    repeller.display()
    attractor.display()
    liquid.display()
    
