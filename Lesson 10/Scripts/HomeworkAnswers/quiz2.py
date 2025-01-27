# Викторина по выбору правильного варианта ответа
# Программа проверяет знания пользователя, задавая ему вопросы и предлагая на выбор ответ из несольких вариантов
# Блоки информации с темой, вопросом, вариантами ответов, правильным ответом, его весом и пояснениями читаются из текстового файла.
# Строки данных в текстовом файлы следуют одна за другой без пропусков
# Структура текстового файла, с которым работает программа:
# 1-я строка содержит название викторины, а далее следуют блоки информации  по следующей схеме:
# <тема вопроса>
# <вопрос>
# <ответ 1>
# <ответ 2>
# ...
# <ответ N>, N не превышает 9
# <порядковый номер правильного варианта ответа>
# <вес ответа - количество баллов, которое дается за правильный ответ>
# <пояснения к выбору правильного варианта ответа>
# Все компоненты в блоке информации по вопросу располагаются каждая на отдельной строке.
# При этом символ "/" внутри строки означает, что при отображении строки в программе в этом месте нужно вставить перевод строки

import sys
import string

RECORD_FILE_NAME = "quiz_record.txt"

class MyRangeError(Exception): pass
class MyEOFError(Exception): pass

def get_integer(message, name="целое число", minimum=None, maximum=None):
    """ (str, str, int, int) -> int
    Запрашивает у пользователя целочисленное значение name с приглашением message и возвращает это значение.
    Контролирует, чтобы введенное значение было строго больше minimum и строго меньше maximum, если эти параметры заданы
    """
    message += ": "
    while True:
        try:
            line = input(message)
            int_val = int(line)
            if (minimum is not None and minimum > int_val) or (maximum is not None and maximum < int_val):
                raise MyRangeError(f"Ожидается значение {name.upper()} между {minimum} и {maximum}")
            return int_val
        except MyRangeError as err:
            print("ОШИБКА.", err)
        except ValueError as err:
            print(f"ОШИБКА. Значение {name.upper()} должно быть целочисленным")

def open_file(file_name, mode, ignore_except=False):
    """ (str, str) -> opened file
    Открывает файл file_name в режиме mode и возвращает файловую переменную, указывающую на этот файл
    или None если файл открыть не удалось при ignore_except == True
    ignore_errors - признак "подавлять ошибки открытия файла", по умолчанию False
    Предусловие: файл file_name должен быть доступен на открытие в заданном режиме mode,
                 иначе, при ignore_except == False, программа завершает свою работу
    """
    try:
        the_file = open(file_name, mode, encoding="UTF8")
    except IOError as err:
        print("Невозможно открыть файл", file_name, err)
        if ignore_except:
            return None
        input("Работа программы будет завершена.\n\nДля выхода нажмите Enter.")
        sys.exit()
    else:
        return the_file

def read_records(file_name):
    """ (str) -> dict of {str user_name : int record}
    Принимает имя файла с рекордами в file_name. Открывает его для чтения, если такой файл существует.
    Если файл рекордов не существует, то возвращается пустой словарь
    Если файл существует и успешно открыт для чтения, то данные из файла рекордов считываются в словарь,
    который и возвращается из функции. Перед выходом из функции файл закрывается.
    Файл должен содержать данные по каждому пользователю на отдельной строке в следующем виде:
    <имя пользователя>:<рекорд>
    """
    records = {}
    rec_file = open_file(file_name, "r", ignore_except=True)
    if rec_file is None:
        return records
    for line in rec_file:
        record_list = line.split(":")
        records[record_list[0]] = int(record_list[1])
    rec_file.close()
    return records

def save_records(file_name, records):
    """ (str, dict of {str:int}) -> None
    Принимает имя файла с рекордами в file_name и рекорды для записи в файл в словаре records.
    Словарь records содержит имя пользователя в ключе и его рекорд в значении элемента.
    Перед выходом из функции файл закрывается
    """
    rec_file = open_file(file_name, "w")
    for user_name in records:
        rec_file.write(user_name + ":" + str(records[user_name]) + "\n")
    rec_file.close()

def next_line(the_file):
    """ (opened_file) -> str
    Возвращает очередную строку из файла. Символ "/" в строке заменяется на "\n", конечные пробельные символы отбрасываются
    """
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line.rstrip()

def next_block(the_file):
    """ (opened_file) -> tuple
    Возвращает очередной блок данных, касающийся одного вопроса викторины, из открытого файла the_file
    Значение возвращается в кортеже следующей структуры: (str topic, str question, list of str answers[], int correct, int weighht, str explanation)
    Если при чтении темы вопроса достигнут конец файла, то все элементы данного кортежа содержат None
    """
    try:
        topic = next_line(the_file)
        if not topic:
            raise MyEOFError()
        
        question = next_line(the_file)
        if not question:
            raise MyEOFError()
        
        answers = []
        line = next_line(the_file)
        while len(line) > 1 and line not in string.digits:
            answers.append(line)
            line = next_line(the_file)
        if not answers or not line:
            raise MyEOFError()
    
        correct = int(line[0])

        weight = next_line(the_file)
        if weight:
            weight = int(weight)
        else:
            raise MyEOFError()
            
        explanation = next_line(the_file) 

    except MyEOFError:
        topic = question = answers = correct = weight = explanation = None

    return topic, question, answers, correct, weight, explanation

def welcome(title, records):
    """ (str, dict of str:str) -> str
    Приветствует пользователя и сообщает ему название викторины из title.
    Если введенное имя пользователя найдено в словаре records, то выводится предыдущее достижение.
    Возвращает имя пользователя, как он его указал в приглашении
    """
    print("\t\tДобро пожаловать в Викторину!\n")
    print("\t", title, "\n")
    user_name = input("\nПредставьтесь пожалуйста: ").strip()
    if user_name in records:
        # сообщить пользователю предыдущий рекорд
        print("Здравствуйте " + user_name + ". Рады снова Вас видеть! Ваш предыдущий рекорд:", records[user_name])
    else:
        # это новый пользователь, просто поздороваться с ним
        print("Здравствуйте " + user_name + "! Попробуйте себя в нашей Викторине")
    print()
    return user_name

def main():
    # открыть файл, считать название викторины из 1-ой строки файла и поприветствововать пользователя
    quiz_file = open_file("py_struct2.txt", "r")
    title = next_line(quiz_file)

    # считать рекорды пользователей из файла с именем RECORD_FILE_NAME в словарь records
    records = read_records(RECORD_FILE_NAME)

    # поздороваться с пользователем
    user_name = welcome(title, records)
    
    # инициализировать счетчики количества заданных вопросов (total) и правильных ответов на них (right), 
    # а также переменную с набранным счетом пользователя (score)
    total = right = score = 0

    # извлечение из файла первого блока <тема, вопрос, ответы, верный вариант, его вес, пояснения>
    topic, question, answers, correct, weight, explanation = next_block(quiz_file)
    while topic is not None:
        # вывод вопроса на экран
        print("Тема", topic)
        print(question)
        for i in range(len(answers)):
            print("\t", i + 1, "-", answers[i])

        # получение ответа
        answer_num = get_integer("Ваш ответ", "ответ", 1, len(answers))

        # проверка ответа
        if answer_num == correct:
            print("\nПравильно!", end=" ")
            right += 1
            score += weight
        else:
            print("\nНеверно.", end=" ")
        print(explanation)
        print("\nВаш текущий счет:", score, "\n")
        total += 1

        # получение следующего блока из файла
        topic, question, answers, correct, weight, explanation = next_block(quiz_file)

    quiz_file.close()

    print("Это был последний вопрос!")
    print(f"Правильных ответов {right} из {total}. Ваш счет: {score}")
 
    # сохранить рекорд пользователя, если он новый или набрал в этом сеансе работы больше очков, чем раньше
    if user_name not in records or score > records[user_name]:
        records[user_name] = score
        save_records(RECORD_FILE_NAME, records)

main()  
input("\n\nДля выхода нажмите Enter.")
