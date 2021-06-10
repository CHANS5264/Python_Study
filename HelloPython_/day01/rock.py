import random

mine = input("가위바위보를 입력하세요")
com = ""
result = ""
ran = random.random()

if ran <= 0.33 :
    com = "가위"
elif ran >= 0.34 and ran <= 0.66 :
    com = "바위"
else :
    com = "보"

if com == "가위" and mine == "가위":
    result = "비김"
elif com == "바위" and mine == "바위":
    result = "비김"
elif com =="보" and mine == "보":
    result = "비김"

if com == "가위" and mine == "바위":
    result = "이김"
elif com == "바위" and mine == "보":
    result = "이김"
elif com =="보" and mine == "가위":
    result = "이김"

if com == "가위" and mine == "보":
    result = "짐"
elif com == "바위" and mine == "가위":
    result = "짐"
elif com =="보" and mine == "주먹":
    result = "짐"
   

print("com : ", com)
print("mine : ", mine)
print("result : ", result)

