# Оператор множетсвенного выбора (switch/select - отсутствуют)

# if expression1:
#     body1
# elif expression2:
#     body2
# elif expression3:
#     body3
# ...
# else:
#     body_else

age = int(input())

if age <= 14: # Читается сверху-вниз, первый правильный и будет выполнен
    print("Age <= 14")
    print("Не пускаем в приложение вообще")
elif age >= 15 and age <= 18:
    print("Age in [15, 18]")
    print("Даем доступ к демо-версии")
elif age > 18 and age <= 45:
    print('Age in [19, 45]')
    print("Полный доступ к приложению")
else: # необязательный блок
    print("Age is large")

print("Done")