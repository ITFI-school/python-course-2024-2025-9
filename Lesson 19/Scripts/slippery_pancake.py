# Ускользающий блин
# Демонстрирует проверку на соприкосновение спрайтов

from superwires import games
import random

games.init(screen_width=1000, screen_height=600, fps=50)

class Pan(games.Sprite):
    """" Сковорода, которую можно мышью перемещать по экрану """
    def update(self):
        """ Перемещает спрайт в позицию, в которой находится указатель мыши """
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()
 
    def check_collide(self):
        """ Проверяет было ли соприкосновение сковороды и блина """
        for pancake in self.overlapping_sprites:
            pancake.handle_collide()


class Pancake(games.Sprite):
    """" Ускользающий блин """
    def handle_collide(self):
        """ Перемещает спрайт блина в случайную позицию на графическом экране """
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)

def main():
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image

    # создаем спрайт для блина
    pancake_image = games.load_image("pancake.bmp")
    pancake_x = random.randrange(games.screen.width)
    pancake_y = random.randrange(games.screen.height)
    the_pancake = Pancake(image=pancake_image, x=pancake_x, y=pancake_y)
    games.screen.add(the_pancake)

    # создаем спрайт для сковороды
    pan_image = games.load_image("pan.bmp")
    the_pan = Pan(image=pan_image,
                  x=games.mouse.x,
                  y=games.mouse.y)
    games.screen.add(the_pan)

    # делаем указатель мыши невидимым
    games.mouse.is_visible = False

    # перенаправляем весь пользовательский ввод в графическое окно
    games.screen.event_grab = True

    games.screen.mainloop()

# поехали!
if __name__ == "__main__":
    main()
