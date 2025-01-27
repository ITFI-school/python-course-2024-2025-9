# Программа принимает в виде аргументов командной строки слово и одно или более имен файлов.
# Выводит имя файла, номер строки и саму строку, содержащую искомое слово
# Демонстрирует использование функции enumerate()

import sys

if len(sys.argv) < 3:
    print("Использование: grepword.py word infile1 [infile2 [... infileN]]")
    sys.exit()

word = sys.argv[1]
for filename in sys.argv[2:]:
    for lino, line in enumerate(open(filename, encoding='utf-8'), start=1):
        if " " + word + " " in line:
            print(f"{filename}:{lino}:{line.rstrip():.40}")
