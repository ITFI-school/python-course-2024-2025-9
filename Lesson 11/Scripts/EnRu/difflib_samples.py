# Пример демонстрирует использование стандартной библиотеки difflib
# Документацию на difflib см. на https://docs.python.org/3/library/difflib.html

from difflib import SequenceMatcher

# SequenceMatcher - базовый тип данных, который выполняет сравнения:
sm_obj = SequenceMatcher(None, "rain", "rainn")
print("'rain' is similar to 'rainn' by", sm_obj.ratio() * 100, "percents")
input("\n\nPress Enter to go to get_close_matches() example.")

# get_close_matches() - функция для сравнения строки с вариантами из списка:
from difflib import get_close_matches
print(help(get_close_matches))

# пример get_close_matches() с коротким списком:
print("\n\nCompare 'rainn' with ['get', 'cat', 'rain', 'brain']:")
print(get_close_matches("rainn", ["get", "cat", "rain", "brain"]))
input("\n\nPress Enter to go to get_close_matches() examples with dictionary from JSON-file.")

# пример get_close_matches() с ключами словаря из JSON-файла,
# ищем не более 5-ти близких слов:
import json
data = json.load(open("dict.json", encoding="UTF8"))
print("\n\nCompare 'rainn' with JSON-file keys:")
print(get_close_matches("rainn", data.keys(), n=5))

# находим самое близкое слово для "rainn" среди ключей словаря:
print("\n\nThe most similar to 'rainn' among JSON-file keys is:")
close_list = get_close_matches("rainn", data.keys())
the_closest = None
if len(close_list):
    the_closest = close_list[0] 
print("<NOT FOUND>" if the_closest is None else the_closest)

# Ищем слово, заведомо отсутствующее в файле dict.json
# Результат поиска - пустой список:
print("\n\nSearching for 'abracadabra' which is definetely absent from JSON-file keys:")
close_list = get_close_matches("abracadabra", data.keys())
the_closest = None
if len(close_list):
    the_closest = close_list[0] 
print("<NOT FOUND>" if the_closest is None else the_closest)

input("\n\nPress Enter to exit.")
