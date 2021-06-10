# multi return 여러값을 return 받을 수 있음

def addmin(a, b):
    return a+b, a-b

sum, min = addmin(6, 7)

print("sum : ", sum)
print("min : ", min)