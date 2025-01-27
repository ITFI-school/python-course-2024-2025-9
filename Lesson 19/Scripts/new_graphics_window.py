# Новое графическое окно
# Демонстрирует создание графического окна с помощью библиотеки superwires

from superwires import games

# Инициализация графического экрана с частотой обновления 50 кадров в секунду
# fps = frames per second
games.init(screen_width=1000, screen_height=600, fps=50)

# запуск основного цикла
games.screen.mainloop()
