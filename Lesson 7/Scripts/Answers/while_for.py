number = 1729
total = 0
while number < 13504:
    total += number
    number += 2

print("WHILE: ", total)

total = 0
for number in range(1729, 13503+1, 2):
    total += number

print("FOR: ", total)
    
