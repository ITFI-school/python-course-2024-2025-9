# Демонстрирует логические операции

print("3 < 4 истинное логическое выражение - напечатается True:")
print(3 < 4)

print("3 > 7 ложное  логическое выражение - напечатается True:")
print(3 > 7)

print("5.8 >= 5.7 - можно сравнивать и числа с плавающей точкой:")
print(5.8 >= 5.7)

print("7 == 7 - в сравнении на точное равенство ОБЯЗАТЕЛЬНО использовать ДВА ЗНАКА РАВНО:")
print(7 == 7)

int_num1 = 7
int_num2 = 8
nums_equal = (int_num1 == int_num2)
print("int_num1 is", int_num1, ", int_num is", int_num2)
print("nums_equal = (int_num1 == int_num2) - теперь в сравнении используются переменные:")
print(nums_equal)

print("grade_math = 80 : выпускник набрал 80 баллов по математике на ЕГЭ")
grade_math = 80
print("grade_math >= 50 : достиг ли он проходного балла при поступлении в МГТУ?")
print(grade_math >= 50)
print("not (grade_math >= 50): он не пройдет даже в МГТУ?")
print(not (grade_math >= 50))
print("not not (grade_math >= 50) : двойное отрицание исключает само себя:")
print(not not (grade_math >= 50))

print("\ngrade_rus = 70 : по русскому языку выпускник получил 70 баллов на ЕГЭ")
grade_rus = 70
print("(grade_math >= 50) and (grade_rus >= 50): проходит ли он по 2-ум предметам?")
print((grade_math >= 50) and (grade_rus >= 50))             

print("\ngrade_ph = 40 : по физике выпускник получил 70 баллов")
print("grade_cs = 80 : а по информатике 80")
grade_ph = 40
grade_cs = 80

print("Принимаем, если сданы обязательные предметы и сдан хотя бы один дополнительный")
print("(grade_math >= 50) and (grade_rus >= 50) and (grade_ph >= 50 or grade_cs >= 50)")
print((grade_math >= 50) and (grade_rus >= 50) and (grade_ph >= 50 or grade_cs >= 50))

input("\n\nНажмите Enter для выхода.")
