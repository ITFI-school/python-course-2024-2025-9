# Эта программа запршивает имя пользователя и здоровается с ним
user_name = input("What is your name? ")
print("Hello " + user_name)

# Необходимо узнать сколько лет пользователю и сообщить через сколько лет
# ему или ей будет 40 лет. Используйте input() и print() для реализации этой задачи
user_age = input("How old are you? ")
age_delta = 40 - int(user_age)
print("You'll be/were 40 in", age_delta, "years")
