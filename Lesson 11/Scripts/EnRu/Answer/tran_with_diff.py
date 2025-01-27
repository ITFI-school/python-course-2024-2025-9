# Демонстрирует запрос и перевод английского слова на русский язык
# с помощью словаря, считанного из JSON-файла.
# Программа не допускает исключения KeyError, если слово не найдено.
# Английское слово для поиска можно вводить в любом регистре.
# Если введено слово, похожее на то, что есть в ключах словаря,
# то программа предупреждает о возможной ошибке пользователя
# и даёт выбрать другое, наиболее вероятное слово

import json
from difflib import get_close_matches

def translate(word, eng_2_rus):
    """ (str, dict of {str:str}) -> (str, str)

    Переводит слово word на английский язык, используя словарь eng_2_rus,
    и возвращает как слово на английском, так и его значение на русском языке
    Предусловие: в словаре eng_2_rus должен быть ключ word или на >= 60%
                 похожее на него слово, иначе возвращается (word, None)
    """
    word = word.lower()
    if word in eng_2_rus:
        # большинство английских слов в словаре набраны в нижнем регистре
        return word, eng_2_rus[word]
    elif word.title() in eng_2_rus:
        # ситуация, когда ищем слова типа "Magnitogorsk", "Friday", "December"
        t_word = word.title()
        return t_word, eng_2_rus[t_word]
    elif word.upper() in eng_2_rus:
        # помогает если ищем слова типа "USA", "TV", "OK"
        up_word = word.upper()
        return up_word, eng_2_rus[up_word]

    # поиск похожих слов
    close_matches = get_close_matches(word, eng_2_rus.keys())
    if close_matches:
        similar_word = close_matches[0]
        confirm = input(f"Did you mean '{similar_word}' instead of '{word}'? Enter 'Y' to confirm: ")
        if confirm in "Yy":
            return similar_word, eng_2_rus[similar_word]

    return word, None


# здесь начинается основная программа
data = json.load(open("dict.json", encoding="UTF8"))

en_word = input("Enter an English word: ")

en_word, ru_word = translate(en_word, data)
if ru_word is None:
    print("Can't find translation for the word '" + en_word + "'")
else:
    print("'" + en_word + "' in Russian means:", ru_word)

input("\n\nPress Enter to exit.")
