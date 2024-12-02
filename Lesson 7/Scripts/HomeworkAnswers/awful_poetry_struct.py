import random
import parts

STROPHE_SIZE = 6  # количество строк стихотворения в одной строфе
DEFAULT_PARTS = 2 # из скольки строк по умолчанию будет генерироваться стих

def choose_word(parts, dup_parts):
    """(list of str, list of str) -> str
    Receive list of words in parts and list of duplicated words per strophe in dup_parts.
    Return a new random word from parts which is not duplicated among the strophe
    """
    word = random.choice(parts)
    while word in dup_parts:
        word = random.choice(parts)
    dup_parts.append(word)
    return word


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
    particle = choose_word(parts.particles, used_parts)
    noun = choose_word(parts.nouns, used_parts)
    verb = choose_word(parts.verbs, used_parts)

    # генерация и вывод строки стихотворения
    if random.randint(0,1) == 0:
        if random.randint(0,2) in (0,1):  # 2/3 случаев когда нет наречий
            adjective = choose_word(parts.adjectives, used_parts);
            print(particle, adjective, noun, verb)
        else:
            print(particle, noun, verb)
    else:
        adverb = choose_word(parts.adverbs, used_parts);
        print(particle, noun, verb, adverb)

    # обработка конца строфы
    if (index + 1) % STROPHE_SIZE == 0:
        used_parts.clear()  # очищаем список использованных частей речи
        print()             # печатаем пустую строку в конце строфы


input("\nPress enter to exit")
