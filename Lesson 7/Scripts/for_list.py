# нужно увеличить каждый элемент списка в два раза

# почему этот код не даст нужный результат?
print("Попытка 1:")
arr = [1, 2, 3]
for item in arr:
    item *= 2
print(arr)

# почему этот код выдает исключение IndexError
print("\nПопытка 2:")
try:
    for petya in arr:
        arr[petya] *= 2
except IndexError as err:
    print(err)
print(arr)

# а этот код - то что нужно
print("\nПопытка 3:")
for index in range(0, len(arr)):
    arr[index] *= 2
print(arr)

input("\nНажмите Enter для выхода")
