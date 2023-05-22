## PIP и сторонние пакеты. Инструкция по установке jupyter notebook

* **PIP** - менеджер установки пакетов в `Python` (`pypi.org` - хранилище всех пакетов среди разработчиков `Python`)

* Для того, чтобы устанавливать пакеты через `pip`:
    1. Проверить, что `pip` установлен : `pip --version` / ИЛИ `python -m pip --version`
    2. Для установки `pip install <package_name>`
    3. Для удаления `pip uninstall <package_name>`

### 0. Настройка pip через proxy

1) Через proxy:

```
pip install --proxy http://username:password@proxy:port <package_name>
или
pip install --proxy https://username:password@proxy:port <package_name>
```

Пример с установкой `jupyter notebook` (параметры username, password, proxy и port уточните у отдела ИБ)
```
pip install --proxy http://evgen:1234pass@123.22.22:8080 notebook
или
pip install --proxy https://evgen:1234pass@123.22.22:8080 notebook
```

2) Или в командной строке можно задать:
```
set HTTP_PROXY=http://username:password@proxy:port
set HTTPS_PROXY=https://username:password@proxy:port
и выполняете
pip install <package_name>
```

Пример с установкой `jupyter notebook` (параметры username, password, proxy и port уточните у отдела ИБ)
```
set HTTP_PROXY=http://evgen:1234pass@123.22.22:8080
set HTTPS_PROXY=https://evgen:1234pass@123.22.22:8080
pip install notebook
```

3) Добавление `trusted hosts`:
```
pip --trusted-host pypi.python.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install --proxy http://username:password@proxy:port <package_name>
```
Пример с установкой `jupyter notebook` (параметры username, password, proxy и port уточните у отдела ИБ)

```
pip --trusted-host pypi.python.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org install --proxy http://evgen:1234pass@123.22.22:8080 notebook
```



4) Забор пакетов из внутреннего хранилища (ниболее удобный и правильный)
* `JFrog` - хранилище `python` пакетов (локальное), откуда также можно брать пакеты как общие , так и кастомные. (Инстуркция по работе с `JFrog` находилась на `Confluence`).
* Инструкция : https://confluence.raiffeisen.ru/pages/viewpage.action?pageId=221850837

###  Доп. команды
* `pip freeze` - показывает все установленные через `pip` в систему пакеты и библиотеки
* `pip uninstall <package_name>` - удалить выбранный пакет

### Проверка работоспособности
Узнать версию (выполнять в cmd/terminal/shell):
```
jupyter notebook --version
```

Запуск (выполнять в cmd/terminal/shell):
```
jupyter notebook
```

ИЛИ

```
python -m notebook
```