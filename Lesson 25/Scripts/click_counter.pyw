# Счетчик щелчков
# Демонстрирует связывание событий с обработчиками

from tkinter import *

class Application(Frame):
    """ GUI-приложение, которое подсчитывает количество нажатий кнопки """ 
    def __init__(self, master_window):
        """ Иницициализирует рамку """
        super().__init__(master_window)  
        self.grid()
        # создаем у объекта атрибут, следящий за количеством нажатий на кнопку
        self.bttn_clicks = 0
        self.create_widget()

    def create_widget(self):
        """ Создает кнопку, на которой отображается количество
            совершенных нажатий
        """
        self.bttn = Button(self)
        self.bttn["text"] = "Количество щелчков: 0"
        # параметр command у кнопки ссылается на метод update_count(),
        # т.е. при нажатии кнопки будет вызываться этот метод
        self.bttn["command"] = self.update_count
        self.bttn.grid()

    def update_count(self):
        """ Увеличивает количество нажатий на единицу и отображает его """
        self.bttn_clicks += 1
        self.bttn["text"] = "Количество щелчков: " + str(self.bttn_clicks)
          

# Основная часть программы

# Создание базового окна и установка его заголовка и размеров
window = Tk()
window.title("Количество щелчков")
window.geometry("300x50")

# Инстанциируем класс Application с родительским элементом window
app = Application(window)

# Старт событийного цикла базового окна
window.mainloop()
