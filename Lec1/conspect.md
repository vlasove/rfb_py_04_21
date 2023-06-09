## Лекция 1. Начало работы

**Python** - интерпретируемый язык программирования.(Язык с вируатльной машиной `PVM` и интерпретацией кода - "построчным выполнением команд").

**Python** - это язык программирования с построчным выполнением команд.

**Python** - это язык с нестрогой типизацией, обладающий широкой кросс-платформенностью.

**Cуществует 2 поколения Python** : `Python2` и `Python3` (`Python2` с 2020 года не поддерживается официально), но эти 2 поколения представляют из себя **совершенно разные языки**. Мы будем изучать `Pyhton3`


### 1. Что нужно? 
* Версия интерпретатора `Python 3.7.x` и выше.
* Любой редактор кода (`VScode`, `Atom`, `Sublime`, `PyCharm`, `VIM`).


### 2. Проверим, что все установилось
* 1) Жмем `Win+R` -> вписываем `cmd`
* 2) В открывшемся окне пишем `python --version`
    * 2.1) Если ничего в ответ на введенное сообщение не получено - это значит, нужно переустановить интерпретатор. При установке не забыть выбрать `ADD TO PATH` (добавление интерпретатора в переменную среды).

* 3) Проверим и редактор кода


### 3. Напишем пару букв
* 1) Запустим интерактивный режим работы интерпретатора: пишем  `python` в `cmd`
* 2) Отключим интерактивный режим : `Ctrl+Z`

* При работе в интерактивном сеансе выполняются абсолютно все команды языка. НО испрвлять/обновлять/заменять участки уже написанного кода становится затруднительно (невозможно). Предложение: будем писать наборы команд понятных интерпретатору в отдельных файлах (с расширением `.py`) ,а а затем подавать их на вход интерпретатору.

### 3. Напишем пару букв
* 1) Запустим интерактивный режим работы интерпретатора: пишем  `python` в `cmd`
* 2) Отключим интерактивынй режим : `Ctrl+Z`

* При работе в интерактивном сеансе выполняются абсолютно все команды языка. НО испрвлять/обновлять/заменять участки уже написанного кода становится затруднительно (невозможно). Предложение: будем писать наборы команд понятных интерпретатору в отдельных файлах (с расширением `.py`) ,а а затем подавать их на вход интерпретатору.


### 4. Файлы .py и скрипты
* Пока будем именовать файлы с расширением `.py` - скриптами.
* Создадим файл `example.py`
* Наполним этот файл каким-либо кодом, понятным `Python`
```
message = "Hello world!!"
result = 10 + 20 * 3

print("Message:", message)
print("Result:", result)
```
* Теперь необходимо открыть консоль в нужном месте : ! Открывайте консоль там, где лежит скрипт. 
* Иначе придется писать полный путь до вашего скрипта!
    * Из другого каталога (папки) :
    ```
    C:\Users\evgen\Desktop>python rfb_py_1_08_11/Lec1/example.py
    ```

### 5. Правила именования файлов .py
* 1) Название файла должно быть понятно ПРЕЖДЕ ВСЕГО ВАМ
* 2) В названиях файла РЕКОМЕНДУЕТСЯ использовать:
    * Латинские символы
    * Цифры
    * Символ `_` нижнего подчеркивания
