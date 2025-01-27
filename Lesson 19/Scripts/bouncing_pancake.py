# Скачущий блин
# Демонстрирует обработку столкновений с границами экрана

from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50) 

# Блин теперь унаследован от Sprite
class Pancake(games.Sprite):
    """ Спрайт 'Скачущий блин' """
    def update(self):  # вызывается на каждой итерации цикла mainloop()
        """ Обращает компоненту скорости, если достигнута граница экрана. """
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
            
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy

def main():
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image

    pancake_image = games.load_image("pancake.bmp")
    # создаем блин также как мы раньше создавали объекты типа Sprite
    the_pancake = Pancake(image=pancake_image,
                          x=games.screen.width/2,
                          y=games.screen.height/2,
                          dx=1,
                          dy=1)
    games.screen.add(the_pancake)

    games.screen.mainloop()

# поехали!
if __name__ == "__main__":
    main()
