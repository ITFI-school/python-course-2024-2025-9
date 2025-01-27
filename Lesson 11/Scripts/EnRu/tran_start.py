# Демонстрирует запрос и перевод английского слова на русский язык
# с помощью словаря, считанного из JSON-файла

import json

def translate(word, eng_2_rus):
    """ (str, dict of {str:str}) -> str

    Переводит слово word на русский язык, используя словарь eng_2_rus,
    и возвращает его значение на русском языке
    Предусловие: в словаре eng_2_rus должен быть ключ word,
                 иначе выбрасывается исключение KeyError
    """
    return eng_2_rus[word]


# здесь начинается основная программа
file_handler = open("dict.json", encoding="UTF8")
data = json.load(file_handler)
file_handler.close()

en_word = input("Enter an English word: ")

print("'" + en_word + "' in Russian means:", translate(en_word, data))

input("\n\nPress Enter to exit.")
