import random
import parts

STROPHE_SIZE = 6  # количество строк стихотворения в одной строфе
DEFAULT_PARTS = 2 # из скольки строф по умолчанию будет генерироваться стих

try:
    count = int(input("How many parts of a poem should I generate? "))
except ValueError as error:
    print("Not a valid input. ", error,
          f"\nDefault poem size will be {DEFAULT_PARTS} strophes")
    count = DEFAULT_PARTS

print("\nI offer you this Awful Poem:\n")

for index in range(count * STROPHE_SIZE):
    particle = random.choice(parts.particles)
    noun = random.choice(parts.nouns)
    verb = random.choice(parts.verbs)

    # вывод строки стихотворения
    if random.randint(0,1) == 0:
        print(particle, noun, verb)
    else:
        adverb = random.choice(parts.adverbs)
        print(particle, noun, verb, adverb)

    # печатаем пустую строку в конце строфы
    if (index + 1) % STROPHE_SIZE == 0:
        print()


input("\nPress enter to exit")
