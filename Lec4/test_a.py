# Решение задачи Q
num_a = float(input())
num_b = float(input())

summ = int(num_a + num_b) # Т.к. по условию гарантируется что сумма - это целое число

if summ % 2 == 0:
    print("ЧЁТНОЕ")
else:
    print("НЕЧЁТНОЕ")