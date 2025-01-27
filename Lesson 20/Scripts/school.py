class Member:
    '''Представляет любого человека в школе.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Создан Member: {0})'.format(self.name))

    def tell(self):
        '''Вывести информацию.'''
        print('Имя: "{0}" Возраст: "{1}"'.format(self.name, self.age), end=" ")


class Teacher(Member):
    '''Представляет учителя.'''
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        print('(Уточнение - это Teacher: {0})'.format(self.name))

    def tell(self):
        super().tell()
        print('Зарплата: "{0:d}"'.format(self.salary))


class Student(Member):
    '''Представляет учащегося.'''
    def __init__(self, name, age, mark):
        super().__init__(name, age)
        self.mark = mark
        print('(Уточнение - это Student: {0})'.format(self.name))

    def tell(self):
        super().tell()
        print('Средний балл: "{0:.2f}"'.format(self.mark))

# основная программа
the_teacher = Teacher("Марь Иванна", 45, 40000)
vasia = Student("Василий Иванович", 36, 3.5)
petya = Student("Петька", 18, 4.2)

print()   # печатает пустую строку

for member in [the_teacher, vasia, petya]:
    member.tell()  # метод tell() работает и для учителя, и для учеников

input("\n\nНажмите Enter, чтобы выйти")
