
subjects = ["biology","math","IT","history","english","geography"]

import random

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
        
    def teach(self, student, topic):
        student.learn(topic, self)


class Student(Member):
    '''Представляет учащегося.'''
    def __init__(self, name, age, mark, intelligence):
        super().__init__(name, age)
        self.mark = mark
        print('(Уточнение - это Student: {0})'.format(self.name))
        self.knowledge  = []
        self.intelligence = intelligence

    def tell(self):
        super().tell()
        print('Средний балл: "{0:d}"'.format(self.mark))
        
    def learn(self, topic, knowledge_src):
        if( isinstance(knowledge_src, Teacher) ):
            self.knowledge.append(topic)
        elif( isinstance(knowledge_src, Student) ):
            if(self.intelligence>=7):
                self.knowledge.append(topic)
        else:
            pass
    
    def forget(self, topic):
        self.knowledge.remove(topic)
    
    @property
    def grade(self):
        knowledge_precent = int( len(self.knowledge) / len(subjects)  * 100)
        if knowledge_precent > 80:
            grade = 5
        elif 80 >= knowledge_precent >= 60:
            grade = 4
        elif 61 >= knowledge_precent >= 50:
            grade = 3
        else:
            grade = 2
            
        return grade 
    
# основная программа
the_teacher = Teacher("Марь Иванна", 45, 40000)
vasia = Student("Василий Иванович", 36, 3, 6)
petya = Student("Петька", 18, 4, 10)

print()   # печатает пустую строку

for member in [the_teacher, vasia, petya]:
    member.tell()  # работает и для учителя, и для учеников - полиморфизм

# Learning
print()

# Teaching Student
def school_day(student, teacher):
    for i in range(0, 4):
        teacher.teach(student,random.choice(subjects))
    
    for i in range(0, 2):
        student.learn(random.choice(subjects),student)
    
    print(student.name,"узнал:",student.knowledge,"\n")
    
    to_forget = random.choice(student.knowledge)
    student.forget(to_forget)
    print(student.name,"забыл:",to_forget,"\n")
    print(student.name,"запомнил:",student.knowledge,"\n")
    print(student.name,"был оценен:",student.grade)
    
school_day(vasia, the_teacher)

input("\n\nНажмите Enter, чтобы выйти")