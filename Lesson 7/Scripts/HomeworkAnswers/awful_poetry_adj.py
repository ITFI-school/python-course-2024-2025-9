import random
import parts

STROPHE_SIZE = 6  # количество строк стихотворения в одной строфе
DEFAULT_PARTS = 2 # из скольки строк по умолчанию будет генерироваться стих

try:
    count = int(input("How many parts of a poem should I generate? "))
except ValueError as error:
    print("Not a valid input. ", error,
          f"\nDefault poem size will be {DEFAULT_PARTS} strophes")
    count = DEFAULT_PARTS

print("\nI offer you this Awful Poem:\n")

# список использованных частей речи
used_parts = []

for index in range(count * STROPHE_SIZE):
    # получение частей речи с исключением дубликатов в рамках одной строфы
    particle = random.choice(parts.particles)
    while particle in used_parts:
        particle = random.choice(parts.particles)

    noun = random.choice(parts.nouns)
    while noun in used_parts:
        noun = random.choice(parts.nouns)

    verb = random.choice(parts.verbs)
    while verb in used_parts:
        verb = random.choice(parts.verbs)

    # пополнение списка использованных частей речи
    used_parts += [particle] + [noun] + [verb]

    if random.randint(0,1) == 0:
        if random.randint(0,2) in (0,1):  # 2/3 случаев когда нет наречий
            adjective = random.choice(parts.adjectives)
            while adjective in used_parts:
                adjective = random.choice(parts.adjectives)
            used_parts.append(adjective)
            print(particle, adjective, noun, verb)
        else:
            print(particle, noun, verb)
    else:
        adverb = random.choice(parts.adverbs)
        while adverb in used_parts:
            adverb = random.choice(adverbs)
        used_parts.append(adverb)
        print(particle, noun, verb, adverb)

    # обработка конца строфы
    if (index + 1) % STROPHE_SIZE == 0:
        used_parts.clear()  # очищаем список использованных частей речи
        print()             # печатаем пустую строку в конце строфы


input("\nPress enter to exit")
