# Взрыв
# Демонстрирует создание анимации

from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50)

space_image = games.load_image("space.jpg", transparent=0)
games.screen.background = space_image

explosion_files = ["explosion1.bmp",
                   "explosion2.bmp",
                   "explosion3.bmp",
                   "explosion4.bmp",
                   "explosion5.bmp",
                   "explosion6.bmp",
                   "explosion7.bmp",
                   "explosion8.bmp",
                   "explosion9.bmp"]
          
explosion = games.Animation(images=explosion_files,  # список графических файлов или предзагруженных картинок
                            x=games.screen.width/2,  # координаты расположения анимации на экране,
                            y=games.screen.height/2, # такие же как у спрайта, т.к. Animation - потомок Sprite
                            n_repeats=0,             # количество повторений анимации, 0 - не переставая
                            repeat_interval=5)       # интервал (количество обновлений экрана) между двумя
                                                     # последовательными членами анимированного ряда
games.screen.add(explosion)

games.screen.mainloop()
