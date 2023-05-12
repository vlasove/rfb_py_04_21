# Предположительно решение задачи A
num_a = float(input())
num_b = float(input())
sign = input()

if sign == "+":
    print(num_a + num_b)
elif sign == "*":
    print(num_a * num_b)
elif sign == "-":
    print(num_a - num_b)
elif sign == "/" and num_b != 0 :
    print(num_a/num_b)
else:
    print("СБОЙ")








#Решение задачи А. Умный калькулятор. 
num_A = float(input())
num_B = float(input())
sign = input()

if sign  =="+":
    print(num_A+num_B)
elif sign  =="-":
    print(num_A-num_B)
elif sign =="*":
    print(num_A*num_B)
elif sign =="/" and num_B != 0:
    print(num_A/num_B)
else: 
    print("СБОЙ")
