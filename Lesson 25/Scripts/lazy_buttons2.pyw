# Бесполезные кнопки
# Демонстрирует создание класса в оконном приложении на основе tkinter

from tkinter import *

class Application(Frame):
    """ GUI приложение с 3-мя кнопками """ 
    def __init__(self, master_window):
        """ Инициализрует рамку """
        super().__init__(master_window)    
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Метод, создающий элементы управления, т.е. 3 бесполезные кнопки """
        # первая кнопка
        self.bttn1 = Button(self, text="Я ничего не делаю!")
        self.bttn1.grid()

        # вторая кнопка
        self.bttn2 = Button(self)
        self.bttn2.grid()	
        self.bttn2.configure(text="И я тоже!")

        # третья кнопка
        self.bttn3 = Button(self)
        self.bttn3.grid()
        self.bttn3["text"] = "И я!"


# Основная часть программы

# Создание базового окна и установка его заголовка и размеров
window = Tk()
window.title("Бесполезные кнопки - 2")
window.geometry("320x100")

# Инстанциируем класс Application с родительским элементом window.
# Application является наследником Frame, поэтому app - это рамка,
# расположенная в базовом окне window
app = Application(window)

# Старт событийного цикла базового окна
window.mainloop()
