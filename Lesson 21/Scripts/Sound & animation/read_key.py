# Чтение с клавиатуры
# Демонстрирует чтение клавиатурного ввода

from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50)

class Ship(games.Sprite):
    """ Спрайт - подвижный космический корабль """
    def update(self):
        """ Перемещает корабль определенным образом, исходя из нажатых клавиш """
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1           
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1
 
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
