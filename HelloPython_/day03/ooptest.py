class Dog:
    
    def __init__(self):
        self.flag_bark = True
    
    def doSergury(self):
        self.flag_bark = False
        
class Bird:
    
    def __init__(self):
        self.x = 5
        self.y = 5
        
    def goToSaeukkang(self,x,y):
        self.x = x
        self.y = y
    
class GaeSae(Dog, Bird):
    def __init__(self):
        Dog.__init__(self)
        Bird.__init__(self)
        
gs = GaeSae()
print(gs.flag_bark)
print(gs.x)
print(gs.y)
gs.doSergury()
gs.goToSaeukkang(50, 50)
print(gs.flag_bark)
print(gs.x)
print(gs.y)