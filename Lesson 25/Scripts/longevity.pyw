# Секрет долгожителя
# Демонстрирует текстовое поле, текстовую область и менеджер размещения Grid

from tkinter import *

class Application(Frame):
    """ GUI приложение, владеющее секретом долголетия. """ 
    def __init__(self, master_window):
        """ Иницициализирует рамку """
        super().__init__(master_window)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создает кнопку, текстовое поле и текстовую область. """
        # метка-инструкция
        self.inst_lbl = Label(self, text="Чтобы узнать секрет долголетия, введите пароль")
        self.inst_lbl.grid(row=0, column=0, columnspan=2, sticky=W)

        # метка около поля ввода пароля
        self.pw_lbl = Label(self, text="Пароль: ")
        self.pw_lbl.grid(row=1, column=0, sticky=W)

        # текстовое поле для ввода пароля      
        self.pw_ent = Entry(self)
        self.pw_ent.grid(row=1, column=1, sticky=W)

        # кнопка отправки значения
        self.submit_bttn = Button(self, text="Узнать секрет", command=self.reveal)
        self.submit_bttn.grid(row=2, column=0, sticky=W)

        # создание текстовой области, в которую будет выведен ответ
        # параметр wrap определяет механизм переноса текста, напечатанного внутри:
        # доступные значения - WORD, CHAR и NONE
        self.secret_txt = Text(self, width=35, height=5, wrap=WORD)
        # сделаем так, чтобы текстовая область разместилась на следующей строке
        # в менеджере размещения и охватила два столбца:
        self.secret_txt.grid(row=3, column=0, columnspan=2, sticky=W)

    def reveal(self):
        """ В зависимости от пароля, введенного в текстовое поле,
        отвечает разными сообщениями в текстовой области
        """
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "Чтобы дожить до 100 лет, нужно сначала дожить до 99, "\
                      "а потом вести себя ОЧЕНЬ осторожно."
        else:
            message = "Вы ввели неправильный пароль, так что я не могу поделиться"\
                      " с вами этой тайной. Она доступна только для избранных"
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)


# Основная часть программы

# Создание базового окна и установка его заголовка и размеров
window = Tk()
window.title("Долгожитель")
window.geometry("350x150")

# Инстанциируем класс Application с родительским элементом window
app = Application(window)

# Старт событийного цикла базового окна
window.mainloop()
