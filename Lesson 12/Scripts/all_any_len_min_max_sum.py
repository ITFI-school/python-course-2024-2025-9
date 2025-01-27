# Демонстрация функций работы с итерабельными объектами.
# Для примера взят список

x_list = [-2, 9, 7, -4, 3]
print("Список:", x_list)

res_tuple = all(x_list), any(x_list), len(x_list), min(x_list), max(x_list), sum(x_list)
print("all(), any(), len(), min(), max(), sum():\n", res_tuple)

x_list.append(0)
print("\nСписок:", x_list)

res_tuple = all(x_list), any(x_list), len(x_list), min(x_list), max(x_list), sum(x_list)
print("all(), any(), len(), min(), max(), sum():\n", res_tuple)

input("\n\nДля выхода нажмите Enter.")
