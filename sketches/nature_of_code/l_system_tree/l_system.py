
class LSystem():
    
    def __init__(self, axiom, rules):
        self.sentence = axiom
        self.rules = rules
        self.generation = 0
        
    
    def generate(self):
        next = []
        for cur in self.sentence:
            replace = cur
            for rule in self.rules:
                if rule.a == cur:
                    replace = rule.b
                    break
            next.append(replace)
        self.sentence = ''.join(next)
        self.generation += 1
        
        
    def generate_random(self):
        next = []
        for cur in self.sentence:
            replace = cur
            for rule in self.rules:
                if rule.a == cur:
                    replace = rule.b[int(random(len(rule.b)))]
                    break
            next.append(replace)
        self.sentence = ''.join(next)
        self.generation += 1
    
