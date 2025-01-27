# Киноман
# Демонстрирует применение флажков

from tkinter import *

class Application(Frame):
    """ GUI-приложение, позволяющее выбирать любимые жанры кино. """
    def __init__(self, master_window):
        """ Иницициализирует рамку """
        super().__init__(master_window)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создает диалоговые элементы, с помощью которых пользователь
        будет выбирать варианты. """
        # создаем метку-описание
        Label(self,
              text = "Укажите ваши любимые жанры кино"
              ).grid(row=0, column=0, sticky=W)

        # создаем метку-инструкцию
        Label(self,
              text = "Выбирайте все, что вам по вкусу:"
              ).grid(row=1, column=0, sticky=W)
        
        # создаем флажок "Комедия" и связанную с ним переменную
        self.likes_comedy = BooleanVar()
        Checkbutton(self,
                    text="Комедия",
                    variable=self.likes_comedy,
                    command=self.update_text
                    ).grid(row=2, column=0, sticky=W)

        # создаем флажок "Ужастик" и связанную с ним переменную
        self.likes_horror = BooleanVar()
        Checkbutton(self,
                    text="Ужастик",
                    variable=self.likes_horror,
                    command=self.update_text
                    ).grid(row=3, column=0, sticky=W)

        # создаем флажок "Боевик" и связанную с ним переменную
        self.likes_action = BooleanVar()
        Checkbutton(self,
                    text="Боевик",
                    variable=self.likes_action,
                    command=self.update_text
                    ).grid(row=4, column=0, sticky=W)

        # текстовая область с результатами выбора пользователя
        self.results_txt = Text(self, width=40, height=5, wrap=WORD)
        self.results_txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """ Обновляет текстовый элемент по мере того,
            как пользователь выбирает любимые киножанры
        """
        likes = ""
        
        if self.likes_comedy.get():
            likes += "Вам нравятся комедии.\n"

        if self.likes_horror.get():
            likes += "Вы не прочь посмотреть ужастик.\n"

        if self.likes_action.get():
            likes += "Вы просто в восторге от боевиков."
      
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, likes)


# Основная часть программы

# Создание базового окна и установка его заголовка и размеров
window = Tk()
window.title("Киноман")

# Инстанциируем класс Application с родительским элементом window
app = Application(window)

# Старт событийного цикла базового окна
window.mainloop()
