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

