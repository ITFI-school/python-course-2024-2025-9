# Спрайт "блин"
# Демонстрирует создание спрайта 

from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50)

wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

# загружаем изображение блина из графического файла в переменную pancake_image
# по умолчанию transparent=True, т.е. изображение прозрачное (его фон не виден)
pancake_image = games.load_image("pancake.bmp")

# создаем спрайт с изображением блина, x и y - координаты центра
pancake_sprite = games.Sprite(image=pancake_image, x=500, y=300)

# добавляем спрайт на графический экран
games.screen.add(pancake_sprite)

games.screen.mainloop()
