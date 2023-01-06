from particle import Particle


class ParticleSystem(object):
    def __init__(self, loc):
        self.origin = loc.get()
        self.particles = []
        
    def add_particle(self):
        self.particles.append(Particle(self.origin))
        
    def apply_force(self, force):
        for particle in self.particles:
            particle.apply_force(force)
            
    def apply_attractor(self, attractor):
        for particle in self.particles:
            force = attractor.attract(particle)
            particle.apply_force(force)
            
    def apply_repeller(self, repeller):
        for particle in self.particles:
            force = repeller.repel(particle)
            particle.apply_force(force)
            
    def apply_liquid(self, liquid):
        for particle in self.particles:
            force = liquid.drag(particle) if liquid.is_inside(particle) else PVector(0, 0)
            particle.apply_force(force) 
            
    def apply_friction(self, friction):
        for particle in self.particles:
            force = friction.friction(particle)
            particle.apply_force(force) 
            
    def run(self):
        self.particles = [p for p in self.particles if p.lifespan > 0]
        for particle in self.particles:
            particle.run()
            
    def check_boundary(self):
        for particle in self.particles:
            particle.check_boundary()
