# подсчёт букв в строке
word = 'letters'

#  ... in set(word) чтобы избежать повторного подсчёта повторяющихся букв
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

# "переворачивание" словаря
dict_abc = {'a': 1, 'b': 2, 'c': 3, 'd': 3}
dict_123 = {val: key for key, val in dict_abc.items()}
print(dict_123)

# словарь из списка с расчётом значений как ключ в квадрате
a_list = [-2, -1, 0, 1, 2, 3, 4, 5]
a_dict = {x: x**2 for x in a_list}
print(a_dict)

input("\n\nДля выхода нажмите Enter.")
