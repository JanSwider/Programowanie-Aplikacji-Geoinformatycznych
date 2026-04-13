import random
import math

# input
a = input("Podaj liczbę: ")
a = float(a)

# losowanie
b = random.random() * 100

print("a =", a, type(a))
print("b =", b, type(b))

# porównania
print(a > b)
print(a > 100 and b > 100)
print(a < 10 or b < 10)

# działania
dod = a + b
ode = a - b
dz = a / b
dzc = a // b
reszta = a % b

# math
sin_a = math.sin(a)
log_b = math.log(b)

# prezentacja (3 miejsca)
print("***** a =", round(a, 3), "*****")
print("***** b =", round(b, 3), "*****")

print("+", round(dod, 3))
print("-", round(ode, 3))
print("/", round(dz, 3))
print("//", round(dzc, 3))
print("%", round(reszta, 3))

print("sin(a)", round(sin_a, 3))
print("log(b)", round(log_b, 3))

# imię
imie = input("Podaj imię: ")

tekst = "Programu używa: " + imie + ", student PK"
print(tekst)

tekst2 = tekst.replace("PK", "AGH")

print("ups pomyłka...")
print(tekst2)

# długość
print("Znaki:", len(tekst2))

# czy jest :
print(":" in tekst2)

# ile a
print("a:", tekst2.count("a"))