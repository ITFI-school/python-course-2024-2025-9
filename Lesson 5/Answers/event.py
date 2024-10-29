import random

name = input("Ваше имя: ")
event = input("Название события?: ")
month = random.randint(1, 12)
hour = random.randint(0, 23)

COST = 1235.2356724

message = """\nУважаемый (ая), {name_place}!
Приглашаем Вас на {event_place}.
Дата и время события: 12.{month_place:02}.2023 {hour_place:02}:00.
Стоимость билета: {cost_place:.2f} руб.
"""
print(message.format(name_place=name, event_place=event.upper(),
                     month_place=month, hour_place=hour,
                     cost_place=COST))


message = f"""\nУважаемый (ая),{name}!
Приглашаем Вас на{event.upper()}.
Дата и время события: 12.{month:02}.2023 {hour:02}:00.
Стоимость билета: {COST:.2f} руб."""

print(message)
