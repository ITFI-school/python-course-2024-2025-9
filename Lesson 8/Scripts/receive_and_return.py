# Принимай - возвращай
# Демонстрирует параметры и возвращаемые значения


def display(message):
    """Печатает то, что получила в параметре message"""
    print(message)

def give_me_five():
    """Возвращает 5"""
    five = 5
    return five

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

# основная часть программы
display("Вам сообщение.\n")

number = give_me_five()
print("Вот что возвратила функция give_me_five():", number)

answer = ask_yes_no("\nПожалуйста введите 'y' или 'n': ")
print("Спасибо что ввели:", answer)

input("\n\nДля выхода нажмите Enter.")
