# Крутящийся спрайт
# Демонстрирует вращение спрайта

from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50)

class Ship(games.Sprite):
    """ Спрайт - вращающийся космический корабль """
    def update(self):
        """ Вращает корабль определенным образом исходя из нажатых клавиш """
        if games.keyboard.is_pressed(games.K_RIGHT):
            # +1 градус по часовой стрелке
            self.angle += 1
        if games.keyboard.is_pressed(games.K_LEFT):
            # -1 градус по часовой стрелке, т.е. +1 градус против часовой стрелки
            self.angle -= 1         

        # присвоить углу наклона спрайта одно из предопределенных значений
        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270
 
def main():  
    space_image = games.load_image("space.jpg", transparent=False)
    games.screen.background = space_image

    ship_image = games.load_image("ship.bmp")
    the_ship = Ship(image=ship_image,
                    x=games.screen.width/2,
                    y=games.screen.height/2)
    games.screen.add(the_ship)

    games.screen.mainloop()

if __name__ == "__main__":
    main()
