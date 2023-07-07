import example.sequence as seq # Пример пользовательской зависимости
import math # Пример использования встроенной зависимости
from example.sequence import Sequence # Совмещаеющая пространства имен прогрузка зависимостей



def main():
    """
    Основная точка входа в приложение
    """
    msg = None
    with open("input.txt", mode="r", encoding="utf-8") as fh:
        msg = fh.read().strip() 
    
    s = Sequence(input_message=msg)
    with open("output.txt", "w") as fh:
        fh.write(str(s.find_max()))



"""
Если данный модуль был вызван
напрямую с консоли - значит выполни все,
что находится в его теле!
Иначе - просто проигнорируй
"""
if __name__ == "__main__": # Метка запускаемого модуля
    main()