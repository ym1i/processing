

class CellularAutomata(object):
    
    def __init__(self, n_col=60, n_row=60, rule_num=90):
        self.n_col = n_col
        self.n_row = n_row
        self.w = width / self.n_col
        self.cells = [[0 for col in range(self.n_col)] for row in range(self.n_row)]
        self.ruleset = self.create_ruleset(rule_num)
        self.cells[0][self.n_col / 2] = 1
            
    def generate(self):
        for j in range(self.n_row - 1):
            for i in range(1, self.n_col - 1):
                left = self.cells[j][i - 1]
                center = self.cells[j][i]
                right = self.cells[j][i + 1]
                self.cells[j + 1][i] = self.rules(left, center, right)        
        
    def rules(self, a, b, c):
        s = '{}{}{}'.format(a, b, c)
        index = int(s, 2)
        
        return self.ruleset[index]
    
    def create_ruleset(self, n):
        ruleset = []
        for i in format(n, '08b'):
            ruleset.append(int(i))
        return ruleset
            
    def render(self):
        for j in range(self.n_row):
            for i in range(self.n_col):
                fill(0) if self.cells[j][i] == 1 else fill(255)
                rect(i * self.w, j * self.w, self.w, self.w)
