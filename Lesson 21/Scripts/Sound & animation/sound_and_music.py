# Звук и музыка
# Демонстрирует воспроизведение звуков и музыкальных файлов

from superwires import games

games.init(screen_width=1000, screen_height=600, fps=50)

# загрузка звукового файла
missile_sound = games.load_sound("missile.wav")

# загрузка музыкального файла
games.music.load("theme.mid")

# инициализация констант для пунктов меню
EXIT, PLAY_MISSILE_SOUND, LOOP_MISSILE_SOUND, STOP_MISSILE_SOUND,\
      PLAY_THEME_MUSIC, LOOP_THEME_MUSIC, STOP_THEME_MUSIC = map(str, range(7))

choice = None
while choice != EXIT:

    print(
    """
    Звук и музыка
    
    0 - Выйти
    1 - Воспроизвести звук ракетного залпа
    2 - Зациклить звук ракетного залпа
    3 - Остановить звук ракетного залпа
    4 - Проиграть музыкальную тему игры
    5 - Зациклить музыкальную тему игры
    6 - Остановить музыкальную тему игры
    """
    )
    
    choice = input("Ваш выбор: ")
    print()

    # выход
    if choice == EXIT:
        print("До свидания.")

    # воспроизведение звука ракетного залпа
    elif choice == PLAY_MISSILE_SOUND:
        missile_sound.play()
        print("Воспроизвожу звук ракетного залпа.")

    # зацикливание звука ракетного залпа
    elif choice == LOOP_MISSILE_SOUND:
        loop = int(input("Сколько еще раз воспроизвести этот звук? (-1 = бесконечно): "))
        missile_sound.play(loop)
        print("Зацикливаю звук ракетного залпа.")

    # остановка звука ракетного залпа
    elif choice == STOP_MISSILE_SOUND:
        missile_sound.stop()
        print("Останавливаю звук ракетного залпа.")

    # воспроизведение музыкальной темы
    elif choice == PLAY_THEME_MUSIC:
        games.music.play()
        print("Исполняю музыкальную тему игры.")

    # зацикливание музыкальной темы
    elif choice == LOOP_THEME_MUSIC:
        loop = int(input("Сколько еще раз вопроизвести эту музыку? (-1 = бесконечно): "))
        games.music.play(loop)
        print("Зацикливаю музыкальную тему игры.")

    # остановка музыкальной темы
    elif choice == STOP_THEME_MUSIC:
        games.music.stop()
        print("Останавливаю музыкальную тему игры.")
                 
    # непонятный пользовательский ввод
    else:
        print("\nИзвините, в меню нет пункта", choice)
  
input("\n\nНажмите Enter чтобы выйти.")
