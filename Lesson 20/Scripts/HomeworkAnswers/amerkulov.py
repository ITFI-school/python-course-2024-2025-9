import random


SUBJ = ["УК РФ", "Орнитология", "Python", "Фехтование", "Бубноведение", ]


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
        
    def teach(self, subj, student):
        if random.randint(0, 2) == 0:
            student.SmartTake()
        else:
            print('{0} обучил {1} знанию {2}'.format(self.name, student.name, subj))
            student.take(random.choice(SUBJ))
            print('---------------------------------')
        
        
        

class Student(Member):
    '''Представляет учащегося.'''
    def __init__(self, name, age, mark):
        super().__init__(name, age)
        self.mark = mark
        self.knowledge = set()
        #Изначально дети уже знают некоторые предметы
        for subject in range(random.randint(1, 3)):
            self.knowledge.add(random.choice(SUBJ))            
        print('(Уточнение - это Student: {0})'.format(self.name))

    def tell(self):
        super().tell()
        print('Средний балл: "{0:.2f}"'.format(self.mark))

 
    def forget(self):
        print('К сожалению {0} забыл что такое {1}'.format(self.name, self.knowledge.pop()))


    def take(self, subj):
        self.knowledge.add(subj)
        if random.randint(0, 2) == 0:
            self.forget()
       
    
    def SmartTake(self):
        subject = random.choice(SUBJ)
        self.knowledge.add(subject)
        if random.randint(0, 2) == 0:
            self.forget()
        print('Сегодня {0} самостоятельно выучил {1}'.format(self.name, subject))
        print('---------------------------------')


# объявление учеников и учителя
the_teacher = Teacher("Марь Иванна", 45, 40000)
vasia = Student("Василий Иванович", 36, 3.12)
petya = Student("Петька", 18, 4.38)
natasha = Student('Наташка', 11, 3.96)


print()   # печатает пустую строку

for _ in range(7):
    try:
        for member in [ vasia, petya, natasha ]:
           if list(member.knowledge) in SUBJ:
               print("{0} узнал все, что ему могла дать школа. Пора а возможно, даже больше".format(member.name))
               member.mark = 5
               del member
           if len(member.knowledge) == 0:
                print("{0} слишком много халтурил. Его отчислили".format(member.name))
                member.mark = 2
                del member
           the_teacher.teach(random.choice(SUBJ), member)
          
    except NameError as err:
           print('Школа опустела. Пора её закрывать')
           break

input("\n\nНажмите Enter, чтобы выйти")
