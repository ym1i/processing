
class Koch():
    
    def __init__(self, command, len, theta):
        self.command = command
        self.len = len
        self.theta = theta
        
    
    def render(self):
        stroke(0, 0, 0)
        for c in self.command:
            if c == 'F':
                line(0, 0, self.len, 0)
                translate(self.len, 0)
            elif c == '':
                translate(self.len, 0)
            elif c == '+':
                rotate(-self.theta)
            elif c == '-':
                rotate(self.theta)
            elif c == '[':
                pushMatrix()
            elif c == ']':
                popMatrix()
        
