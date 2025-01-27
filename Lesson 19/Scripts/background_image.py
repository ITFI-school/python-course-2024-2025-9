# Фоновая картинка
# Демонстрирует привязку фоновой картинки к графическому экрану

from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50)

# загрузка изображения из файла wall.jpg в переменную wall_image в памяти
# transparent = False т.к. это фоновое изображение, которое не должно "просвечивать"
wall_image = games.load_image("wall.jpg", transparent=False)

# для отображения картинки присвоим переменную с изображением
# свойству background объекта screen
games.screen.background = wall_image

games.screen.mainloop()
