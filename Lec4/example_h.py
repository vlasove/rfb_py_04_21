# Синонимическое неявное приведение логических выражений

age = 10

# Если условное выражение <=> int
# То любое != 0 значение ~ True
# 0 значение ~ False
if age:
    print("Позитивный случай")
else:
    print("Альтернативный случай")

# Если условное выражение <=> float
# То любое != 0.0 значение ~ True
# 0.0 значение ~ False

# Если условное выражение <=> str
# То любое != "" значение ~ True
# "" значение ~ False

# Если условное выражение <=> NoneType
# None ~ False
# not None ~ True




# Обсчет приоритетов при вычислении логического выражения

age = int(input())
 

# A and B
# True and True => True
# False and True => False
# False and False => False
# True and False = > False

if age >= 18 and 1/0: # Если левая часть False - правая не вычисляется
    print("Позитивный случай с приоритетом and")
else:
    print("Альтернативный случай с приоритетом and")

# A or B
# True or True => True
# True or False => True
# False or True => True
# False or False => False

if age >= 18 or 1/0: # Если левая часть True - правая не вычисляется
    print("Позитивный случай с приоритетом or")
else:
    print("Альтернативный случай с приоритетом or")
