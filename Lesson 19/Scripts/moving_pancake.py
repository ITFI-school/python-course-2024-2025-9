# Летающий блин
# Демонстрирует движущийся спрайт

from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50) 

wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

pancake_image = games.load_image("pancake.bmp")

# Для оживления спрайта нужно указать dx - изменение абсциссы объекта за единицу времени,
# в качестве которой выступает один цикл mainlooр() и dy - изменение ординаты объекта
the_pancake = games.Sprite(image=pancake_image,
                           x=games.screen.width/2,
                           y=games.screen.height/2,
                           dx=1,   # просто указали ненулевые значения
                           dy=1)   # в атрибутах dx и dy для спрайта
games.screen.add(the_pancake)

games.screen.mainloop()
