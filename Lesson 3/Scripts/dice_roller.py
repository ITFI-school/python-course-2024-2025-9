# Модель броска игральных костей
# Демонстрирует генерацию случайных чисел

import random

# создаем случайные числа из диапазона 1 - 6 для первого игрока
player1_die1 = random.randint(1, 6) 
player1_die2 = random.randrange(6) + 1

player1_total = player1_die1 + player1_die2
print("При броске первого игрока выпало", player1_die1, "и", player1_die2, "очков, в сумме", player1_total)

# создаем случайные числа из диапазона 1 - 6 для второго игрока
player2_die1 = random.choice( [1, 2, 3, 4, 5, 6] ) 
player2_die2 = int(random.random() * 6) + 1

player2_total = player2_die1 + player2_die2
print("При броске второго игрока выпало", player2_die1, "и", player2_die2, "очков, в сумме", player2_total)

input("\n\nНажмите Enter для выхода")
