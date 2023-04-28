# Форматирование строк и изменение стандартного поведения print()
name = "Bobby"
last_name = "Johnson"
age = "25"

# Форматированные строки - f-strings
message = f"Hello! My name is '{name}', my lastname is !{last_name}!, age is {age}"
print(message)

# Еще один пример
word_a = "###"
word_b = "$$$"
word_c = "@@@"

new_message = f"{word_a}{word_b}{word_c}"
print(new_message)

# TODO!
# Изменение стандартных параметров print()
print("=======НЕПОВТОРИМЫЙ ОРИГИНАЛ============")
print("a", "b", "c") # -> stdout "a b c\nd e f\n"
print("d", "e", "f")
print("=======ЖАЛКАЯ ПОРОДИЯ===================")
# print("a", "b", "c", sep="#oOo#", end="\n")
# print("a", "b", "c", sep=" ", end="END_OF_LINE")
# print("d", "e", "f", sep="!", end="\n")
print("a", "b", "c",  end="END_OF_LINE") # stdout -> "a b cEND_OF_LINEd!e!f\n
print("d", "e", "f", sep="!")

face_mask = "1234"
second_block = "4322"
third_block = "5454"
bank_mask = "9882"

card_num = f"{face_mask} {second_block} {third_block} {bank_mask}"
print(card_num)