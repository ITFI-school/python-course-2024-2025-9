# Киноман
# Демонстрирует применение переключателей

from tkinter import *

class Application(Frame):
    """ GUI-приложение, позволяющее выбирать один любимый жанр кино. """
    def __init__(self, master_window):
        """ Иницициализирует рамку """
        super().__init__(master_window)  
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создает диалоговые элементы, с помощью которых пользователь
        будет выбирать один вариант. """
        # создаем метку-описание
        Label(self,
              text="Укажите ваш любимый жанр кино"
              ).grid(row=0, column=0, sticky=W)

        # создаем метку-инструкцию
        Label(self,
              text="Выберите ровно один:"
              ).grid(row=1, column=0, sticky=W)

        # переменная для хранения сведений о единственном любимом жанре
        self.favorite = StringVar()
        self.favorite.set(None)

        # создаем переключатель "Комедия" и связываем его с переменной
        Radiobutton(self,
                    text="Комедия",
                    variable=self.favorite,
                    value="комедия.",
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)

        # создаем переключатель "Ужастик" и связываем его с переменной
        Radiobutton(self,
                    text="Ужастик",
                    variable=self.favorite,
                    value="ужастик.",
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        # создаем переключатель "Боевик" и связываем его с переменной
        Radiobutton(self,
                    text="Боевик",
                    variable=self.favorite,
                    value="боевик.",
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)

        # текстовая область с результатами выбора пользователя
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """ Обновляет текстовый элемент по мере того,
            как пользователь выбирает любимый киножанр
        """
        message = "Ваш любимый киножанр - "
        message += self.favorite.get()
            
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, message)

# Основная часть программы

# Создание базового окна и установка его заголовка и размеров
window = Tk()
window.title("Киноман - 2")

# Инстанциируем класс Application с родительским элементом window
app = Application(window)

# Старт событийного цикла базового окна
window.mainloop()
