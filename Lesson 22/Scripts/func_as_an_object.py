# Программа демонстрирует работу с функциями как с полноправными объектами
# Функции в Python равны с другими объектами 
# Говорят, что они тоже являются ОБЪЕКТАМИ ПЕРВОГО КЛАССА

# простая функция
def square(x):
    return x * x
print("square(2):", square(2))
print("square(4):", square(4))

# еще одно имя (алиас) для той же самой простой функции
square_too = square
print("square_too(2):", square_too(3))
print("square_too(5):", square_too(5))

# функции можно хранить, присваивать переменным, даже составным, а потом вызывать их
seq_of_func = [abs, str, print, square, square_too]
for func in seq_of_func:
    print(func(-5))

input("\n\nДля выхода нажмите Enter.")
