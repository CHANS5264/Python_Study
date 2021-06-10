class Animal:
  
    def __init__(self):
        self.age = 1
     
    def getOlder(self):
        self.age += 1

class Human(Animal):
    #전역변수
    def __init__(self):
        super().__init__()
        self.skill_lang = 0
        
    def learnFromMama(self):
        self.skill_lang += 1
        
# ani = Animal()
# print(ani.age)
# ani.getOlder()
# print(ani.age)

# hum = Human()
# print(hum.skill_lang)
# hum.learnFromMama()
# print(hum.skill_lang)

hum = Human()
print(hum.age)
print(hum.skill_lang)
hum.getOlder()
hum.learnFromMama()
print(hum.age)
print(hum.skill_lang)

