### python3 tail.py [-f] path
#### 1. Описание
Приложение Python CLI, аналогичное Linux-утилите tail с поддержкой функционала мониторинга файла.
Реализовано скриптом tail.py:
```
usage: tail.py [-f] path

Python analog for linux tail function, Ctrl+C to exit

positional arguments:
  path        path to file

optional arguments:
  -h, --help  show this help message and exit
  -f          file monitoring
```

#### 2. Пример работы
В качестве генератора проверочного файла предлагается использовать скрипт file_writer.py, осуществляющий
запись сгенерированной строки в файл test_file с периодом 0-1 секунду.
```
python3 file_writer.py
```

Запуск приложения в стандартном режиме:
```
python3 tail.py test_file
```

Запуск приложения в режиме мониторинга:
```
python3 tail.py -f test_file
```
