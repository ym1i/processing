from particle_system import ParticleSystem
from repeller import Repeller
from attractor import Attractor
from liquid import Liquid


def setup():
    global ps, repeller, mover, liquid, attractor, friction, gravity
    
    size(640, 360)
    ps = ParticleSystem(PVector(width / 2, 50))
    repeller = Repeller(width / 2, height - 10)
    attractor = Attractor(width / 2, 100)
    liquid = Liquid(0, height / 2, width, height / 4, 0.1)
    
def draw():
    global ps
    background(255)
    
    ps.add_particle()
    
    gravity = PVector(0, 0.02)
    ps.apply_force(gravity)
    ps.apply_repeller(repeller)
    ps.apply_attractor(attractor)
    ps.apply_liquid(liquid)
    
    ps.run()
    ps.check_boundary()
    
    repeller.display()
    attractor.display()
    liquid.display()
    
