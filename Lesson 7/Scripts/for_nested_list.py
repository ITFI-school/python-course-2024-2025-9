# нужно рассчитать средний балл по каждому предмету

# список, содержащий списки с баллами по предметам
grades = [[70, 75, 80], [70, 80, 90, 100], [80, 100]]

# например, первый элемент списка - это оценки за английский
grades_eng = grades[0]

# посчитаем средний балл по английскому
total = 0
for mark in grades_eng:
    total = total + mark
print("Средний балл по английскому:", total/len(grades_eng))

# посчитаем средние баллы по всем предметам, используя вложенный цикл
averages = []
for grades_list in grades:
    # посчитать среднее каждого элемента в grades[] и добавить его в averages[]
    total = 0
    for mark in grades_list:
        total = total + mark

    averages.append(total / len(grades_list));

print("Средние баллы по всем предметам:", averages)

input("\nНажмите Enter для выхода")
