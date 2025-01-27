# Подвижная сковорода
# Демонстрирует ввод с помощью мыши

from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50)

class Pan(games.Sprite):
    """" Сковорода, которую можно мышью перемещать по экрану """
    def update(self):
        """ Перемещает объект в позицию указателя мыши """
        self.x = games.mouse.x
        self.y = games.mouse.y

def main():
    wall_image = games.load_image("wall.jpg", transparent=False)
    games.screen.background = wall_image

    # создаем спрайт-сковородку и добавляем ее на экран
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
