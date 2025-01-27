# Подсчитывает как часто встречается то или иное слово в текстовых файлах,
# принимаемых через параметры командной строки

import collections
import string
import sys

# объявление словаря со значениями по умолчанию равными целочисленному нулю
words = collections.defaultdict(int)

# строка символов, которые отбрасываются слева и справа для каждого слова в файле
strip = string.whitespace + string.punctuation + string.digits + "\"'"

for filename in sys.argv[1:]:    # цикл по файлам, переданным в параметрах запуска
    for line in open(filename):      # цикл по строкам внутри файла
        for word in line.lower().split():  # цикл по словам внутри каждой строки
            word = word.strip(strip)
            if len(word) > 2:
                words[word] += 1

for word in sorted(words):
    print(f"Слово '{word}' встречается раз: {words[word]}")
