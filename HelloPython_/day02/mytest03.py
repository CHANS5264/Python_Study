# 0~1000사이 3의 배수가 아닌 수의 합
sum = 0

for i in range(1, 1001):
    if i%3 != 0 :
        sum += i

print("sum : " ,sum)