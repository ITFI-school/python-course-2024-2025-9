def slow(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                x = i * j * k

def not_fast_multi(n):
    for i in range(n):
        for j in range(n):
            slow(n)

def not_fast_add(n):
    for i in range(n):
        for j in range(n):
            x = i * j

def multiply_complexity(n):
    not_fast_multi(n)

def add_complexity(n):
    slow(n)
    not_fast_add(n)
