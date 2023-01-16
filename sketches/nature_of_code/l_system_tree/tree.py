
class Tree():
    
    def __init__(self, command, len=200, theta=radians(45)):
        self.command = command
        self.len = len
        self.theta = theta
        
    
    def render(self):
        for c in self.command:
            random_len = self.len + random(-1, 1) * self.len * 0.5
            random_theta = self.theta + random(-1, 1) * self.theta * 0.5
            random_theta *= int(random(-2, 2))
            if c == 'F':
                # line(0, 0, 0, self.len)
                # translate(0, self.len)
                stroke(0)
                line(0, 0, 0, random_len)
                translate(0, random_len)
            elif c == 'A':
                #pushMatrix()
                stroke('#00AA00')
                line(0, 0, 0, random_len * 2)
                #popMatrix()
                translate(0, random_len * 2)
            elif c == '+':
                # rotate(-self.theta)
                rotate(-random_theta)
            elif c == '-':
                # rotate(self.theta)
                rotate(random_theta)
            elif c == '[':
                pushMatrix()
            elif c == ']':
                popMatrix()
        
