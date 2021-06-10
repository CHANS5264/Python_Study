# 첫 수를 입력하세요
# 끝 수를 입력하세요
# 배수를 입력하세요
# 배수의 합을 구하세요

a = int(input("첫 수를 입력하세요(작은 수) : "))
b = int(input("끝 수를 입력하세요(큰 수) : "))
bae = int(input("배수를 입력하세요 : "))

sum = 0

for i in range(a, b+1):
    if i%bae == 0:
        sum += i

print(bae, "의 배수의 합 : ", sum)
