# Вот так результат!
# Демонстрирует отображение текста на графическом экране

from superwires import games, color

games.init(screen_width=1000, screen_height=600, fps=50)

wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

# создаем текстовый объект, отображающий крупный счет
# и добавляем его на экран в правый верхний угол,
# Text - потомок класса Sprite, имеет все его свойства,
# а также расширяет набор свойств Sprite собственными:
# value - значение, отображаемое как текст,
# size - высота текста в пикселях, color - цвет текста
score = games.Text(value=1756521,
                   size=60,
                   color=color.black,
                   x=910,
                   y=30)
games.screen.add(score)

games.screen.mainloop()
