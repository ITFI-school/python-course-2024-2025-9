class Test:
    def display(self):
        print ("Это родительский класс Test")

class Test2(Test):
    def display(self):
        super().display()
        print ("Это дочерний класс Test2")

what_print = Test2()
what_print.display()
