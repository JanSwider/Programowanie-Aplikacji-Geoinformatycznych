import random

# losowanie 1 (random -> int 1-100)
liczba1 = int(random.random() * 100) + 1

# losowanie 2
liczba2 = random.randint(1, 100)

print("Liczby:", liczba1, liczba2)

# typy
print(type(liczba1), type(liczba2))

# porównanie
if liczba1 > liczba2:
    print("Pierwsza większa")
elif liczba2 > liczba1:
    print("Druga większa")
else:
    print("Równe")