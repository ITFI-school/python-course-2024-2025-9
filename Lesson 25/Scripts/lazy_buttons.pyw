# Бесполезные кнопки
# Демонстрирует создание кнопок

from tkinter import *

# Создание базового окна и установка его заголовка и размеров
window = Tk()
window.title("Бесполезные кнопки")
window.geometry("300x85")

# Внтури окна создается рамка для размещения других элементов
app = Frame(window)
app.grid()

# Создание кнопки внутри рамки
bttn1 = Button(app, text="Я ничего не делаю!")
bttn1.grid()

# Создание второй кнопки внутри рамки
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text="И я тоже!")

# Создание третьей кнопки внутри рамки
bttn3 = Button(app)
bttn3.grid()
bttn3["text"] = "И я!"

# Старт событийного цикла базового окна
window.mainloop()
