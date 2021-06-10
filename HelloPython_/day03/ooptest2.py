class Terran:
    def __init__(self):
        print("생성자")
        
    def __del__(self):
        print("소멸자")
    
    def __str__(self):
        return "ykbabo"    
# tr = Terran()
# 소멸자는 for문이 끝난 후에 나타남
# for i in range(2):
#     print(i)

# for i in range(2):
#     tr = Terran()

print(Terran())