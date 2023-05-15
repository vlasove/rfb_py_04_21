# Условно-бесконечный цикл while

# Реализовать простейший валидатор электронный почты в приложении
# Считаем почту валидной если:
# 1) имеется точка
# И 2) имеется собачка
# Ввод осуществлятся с консоли
# Количество попыток не ограничено
# Проверка считается успешной если 1) и 2) выполнены => работа программы должна
# завершиться 

while True:
    email = input()
    if "." in email and "@" in email:
        print("Email is valid")
        break
    else:
        print("Evail invalid. Try again!")

# break - операторное слово, которое может быть использовано ТОЛЬКО в теле цикла (или вложено в его часть),
# которое, ОСТАНАВЛИВАЕТ ТЕКУЩУЮ ИТЕРАЦИЮ И ПЕРЕДАЕТ УПРАВЛЕНИЕ ПЕРВОЙ КОМАНДЕ, СТОЯЩЕЙ ЗА ПРЕДЕЛЕАМИ ЦИКЛА!

# continue - -//- ОСТАНАВЛИВАЕТ ТЕКУЩУЮ ИТЕРАЦИЮ И ПЕРЕДАЕТ УПРАВЛЕНИЕ СЛЕДУЮЩЕЙ ИТЕРАЦИИ!


i = 0
while i < 10:
    i += 1 # i = i + 1
    if i % 2 == 0:
        continue
    else:
        print("I is odd:", i)
    print("Another line")
