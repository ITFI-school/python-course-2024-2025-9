# Странная считалка
# Демонстрирует работу команд break и continue

count = 0
while True:      # бесконечный цикл ???!!!
    count += 1
    # без паники - цикл завершится, когда count примет значение больше 10
    if count > 10:
       break
    # пропустить 5
    if count == 5:
        continue
    print(count)
    
input("\nНажмите Enter для выхода.")
