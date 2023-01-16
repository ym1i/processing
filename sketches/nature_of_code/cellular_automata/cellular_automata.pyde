from ca import CellularAutomata


def setup():
    size(600, 600)
    background(255)
    
    ca = CellularAutomata(60, 60, 99)
    ca.generate()
    ca.render()
