# Программа считывает входящие текстовые файлы, переданные через командную строку, 
# и создает соответствующие им .nb файлы без пустых строк

import os
import sys


def read_data(filename):
    lines = []
    file_handler = None
    try:
        file_handler = open(filename, encoding="utf8")
        for line in file_handler:
            if line.strip():
                lines.append(line)
    except (IOError, OSError) as err:
        print(err)
        return []
    finally:
        if file_handler is not None:
            file_handler.close()
    return lines


def write_data(lines, filename):
    file_handler = None
    try:
        file_handler = open(filename, "w", encoding="utf8")
        for line in lines:
            file_handler.write(line)
    except EnvironmentError as err:
        print(err)
    finally:
        if file_handler is not None:
            file_handler.close()


if len(sys.argv) < 2:
    print("usage: no_blanks.py infile1 [infile2 [... infileN]]")
    sys.exit()

for filename in sys.argv[1:]:
    lines = read_data(filename)
    if lines:
        write_data(lines, os.path.splitext(filename)[0] + ".nb")
