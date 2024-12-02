# подсчёт букв латинского алфавита в строке

string = input ("Enter a string: ")
count = 0
for char in string:
    if "a" <= char <= "z" or "A" <= char <= "Z":
        count += 1
print ( count )

input("\n\nPress enter to exit")
