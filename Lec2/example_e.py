# Решение задачи F
# Поток ввода стандартный (STDIN)
name = input("Введите имя:") #-> всегда возвращает строку
last_name = input("Введите фамилию:")
age = input("Введите возраст:")

msg = f"Имя: {name} , Фамилия: {last_name} , Возраст: {age} . Студент BPS"
print(msg)


# Образец для задачи H
first_word = input()
second_word = input()
third_word = input()
fourth_word = input()
general_word = input()

print(f"{fourth_word} - {general_word}")
print(f"{third_word} - {general_word}")
print(f"{second_word} - {general_word}")
print(f"{first_word} - {general_word}")