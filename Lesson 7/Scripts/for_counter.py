# Демонстрирует использование функции range() с циклом for

print("Считаем:")
for i in range(10):
    print(i)

print("\n\nСчитаем с шагом 5:")
for i in range(0, 50, 5):
    print(i, end=" ")

print("\n\nСчитаем в обратном порядке:")
for i in range(10, 0, -1):
    print(i, end=" ")

input("\n\nНажмите Enter для выхода")
