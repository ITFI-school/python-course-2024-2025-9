# Демонстрирует запрос и перевод английского слова на русский язык
# с помощью словаря, считанного из JSON-файла.
# Программа не допускает исключения KeyError, если слово не найдено.
# Английское слово для поиска можно вводить в любом регистре

import json

def translate(word, eng_2_rus):
    """ (str, dict of {str:str}) -> str

    Переводит слово word на английский язык, используя словарь eng_2_rus,
    и возвращает его значение на русском языке
    Предусловие: в словаре eng_2_rus должен быть ключ word,
                 иначе возвращается None
    """
    word = word.lower()
    if word in eng_2_rus:
        return eng_2_rus[word]
    else:
        return None


# здесь начинается основная программа
data = json.load(open("dict.json", encoding="UTF8"))

en_word = input("Enter an English word: ")

ru_word = translate(en_word, data)
if ru_word is None:
    print("Can't find translation for the word '" + en_word + "'")
else:
    print("'" + en_word + "' in Russian means:", ru_word)

input("\n\nPress Enter to exit.")
