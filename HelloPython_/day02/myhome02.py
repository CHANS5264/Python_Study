#첫 수를 입력하세요 - 작은수
#끝 수를 입력하세요 - 큰수
#두 수의 사이의 합은? 1, 5 => 1+2+3+4+5
a = int(input("첫 수를 입력하세요(작은 수) : "))
b = int(input("끝 수를 입력하세요(큰 수) : "))


sum = 0


# for i in range(a, b+1):
#      sum += i
#
# print(a, "~", b, "까지 합 : ", sum)

arr = range(int(a), int(b)+1)

for i in arr :
    sum += i;

print("합은 {}입니다.".format(sum))