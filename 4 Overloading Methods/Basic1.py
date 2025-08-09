class Calculator(object):
    def __init__(self, x = 0 , y = 0):
        self.x = x
        self.y = y
        
    def __add__(self, p):
        return Calculator(self.x + p.x ,  self.y + p.y)
    
    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'
    
p1 = Calculator(3, 4)
p2 = Calculator(4, 2)
p3 = Calculator(3, 7)
p4 = Calculator(5, 4)

total = p1 + p2
total2 = p1 + p2 + p3
print(total, total2)
