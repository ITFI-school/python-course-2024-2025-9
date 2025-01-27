# Демонстрирует запрос и перевод английского слова на русский язык
# с помощью словаря, считанного из JSON-файла.
# Программа не допускает исключения KeyError, если слово не найдено.
# Английское слово для поиска можно вводить в любом регистре.
# Если введено слово, похожее на то, что есть в ключах словаря,
# то программа предупреждает о возможной ошибке пользователя
# и даёт выбрать другое, наиболее вероятное слово

import sys
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
    elif word.capitalize() in eng_2_rus:
        # ситуация, когда ищем слова типа "Magnitogorsk", "Friday", "December"
        cap_word = word.capitalize()
        return t_word, eng_2_rus[cap_word]
    elif word.upper() in eng_2_rus:
        # помогает если ищем слова типа "USA", "TV", "OK"
        up_word = word.upper()
        return up_word, eng_2_rus[up_word]

    # поиск похожих слов
    close_matches = get_close_matches(word, eng_2_rus.keys())
    if len(close_matches) > 0:
        similar_word = close_matches[0]
        confirm = input(f"Did you mean '{similar_word}' instead of '{word}'? Enter 'Y' to confirm: ").strip()
        if confirm.lower() == "y":
            return similar_word, eng_2_rus[similar_word]

    return word, None


def delete_term(p_dict):
    """(dict {str:str}) -> NoneType

    Запрашивает английское слово у пользователя и удаляет его из словаря p_dict
    """
    term = input("Какое английское слово вы хотите удалить из словаря?: ").strip()
    en_word, ru_word = translate(term, data) 
    if ru_word is None:
        print("Невозможно удалить слово '" + term + "' т.к. оно отсутствует в словаре.")
    else:
        del p_dict[en_word]
        print("Слово '" + en_word + "' удалено")


def add_term(p_dict):
    """(dict {str:str}) -> NoneType

    Добавляет английское слово, введенное пользователем, в словарь p_dict
    """
    term = input("Какое слово на английском языке вы хотите добавить?: ").strip()
    if term not in p_dict:
        definition = input("Укажите перевод этого слова на русский язык: ")
        p_dict[term] = definition
        print("Слово '" + term + "' добавлено в словарь.")
    else:
        print("Такое слово уже есть! Но вы можете изменить его перевод.")


def change_term(p_dict):
    """(dict {str:str}) -> NoneType

    Запрашивает английское слово у пользователя, ищет его в словаре p_dict
    и позволяет пользователю переопределить его значение
    """
    term = input("Какое английское слово вы хотите переопределить?: ").strip()
    en_word, ru_word = translate(term, data) 
    if ru_word is None:
        print("Такого слова пока нет! Попробуйте добавить его в словарь.")
    else:
        print("Сейчас '" + en_word + "' обозначает", ru_word)
        definition = input("Впишите ваш перевод на русский: ")
        p_dict[en_word] = definition
        print("Перевод слова '" + en_word + "' переопределен.")


def find_term(p_dict):
    ''' (dict {str:str}) -> NoneType

    Ищет значение термина, введеного пользователем
    '''
    en_word = input('Введите английское слово, перевод которого вы хотите найти: ').strip()
    en_word, ru_word = translate(en_word, data) 
    if ru_word is None:
        print("В словаре не содержится '" + en_word + "'")
    else:
        print("'" + en_word + "' на русском языке означает:", ru_word, '\n')


def save_dict(p_dict):
    '''(dict) -> NoneType
        Запрашивает у пользователя словарь и сохраняет его в файл
    '''
    with open ('dict.json', 'w', encoding="UTF8") as file:
        json.dump(p_dict, file, ensure_ascii=False)
    print('Вы успешно сохранили словарь\n')


# здесь начинается основная программа
EXIT, FIND, ADD, CHANGE, DELETE, SAVE = map(str, range(6))

data = json.load(open("dict.json", encoding="UTF8"))

choice = None
while choice != EXIT:

    print('''
        Англо-русский словарь:
        0 - Выйти
        1 - Найти толкование термина
        2 - Добавить термин
        3 - Изменить толкование термина
        4 - Удалить термин
        5 - Сохранить словарь\n''')

    choice = input("Ваш выбор: ").strip()
    print()

    # выход
    if choice == EXIT:
        print("До свидания.")

    # поиск перевода
    elif choice == FIND:
        find_term(data)       

    # добавление английского слова с переводом
    elif choice == ADD:
        add_term(data)

    # задание нового перевода для имеющегося английского слова
    elif choice == CHANGE:
        change_term(data)

    # удаление английского слова вместе с его переводом из словаря
    elif choice == DELETE:
        delete_term(data)

    # сохранение слова в файле
    elif choice == SAVE:
        save_dict(data)
        
    # непонятный ввод пользователя
    else:
        print("Извините, в меню нет такого пункта", choice, "\n")
