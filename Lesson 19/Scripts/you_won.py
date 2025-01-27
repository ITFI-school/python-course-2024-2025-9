# Победа!
# Демонстрирует вывод исчезающего сообщения на экран

from superwires import games, color

games.init(screen_width=1000, screen_height=600, fps=50)

wall_image = games.load_image("wall.jpg", transparent=False)
games.screen.background = wall_image

# разместим сообщение красного цвета, которое исчезнет через 250 кругов главного цикла
# Message - это потомок класса Text, т.е. обладает всеми его свойствами, а также:
# lifetime - принимает целое число, означающее количество циклов mainlоор(),
#            в течение которых сообщение будет висеть на экране,
#            по умолчанию = 0, т.е. нет саморазрушения объекта
# after_death - ссылка на функцию, которая будет вызвана, когда сообщение исчезнет
won_message = games.Message(value="Победа!",
                            size=100,
                            color=color.red,
                            x=games.screen.width/2,   # в центре по оси X
                            y=games.screen.height/2,  # и в центре по оси Y
                            lifetime=250,
                            after_death=games.screen.quit)

games.screen.add(won_message)

games.screen.mainloop()
