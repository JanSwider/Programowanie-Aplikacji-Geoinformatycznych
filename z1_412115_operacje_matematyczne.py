import math

# 1.
liczba = 453
dzielnik = 5

wynik_dzielenia = liczba / dzielnik
wynik_dzielenia_calkowitego = liczba // dzielnik
reszta_z_dzielenia = liczba % dzielnik

print("1. Dzielenie liczby 453 przez 5:")
print("Dzielenie:", wynik_dzielenia)
print("Dzielenie całkowite:", wynik_dzielenia_calkowitego)
print("Reszta z dzielenia:", reszta_z_dzielenia)
print()

# 2. 
a1 = 35
a2 = 82

print("2. Zadeklarowane liczby:")
print("a1 =", a1)
print("a2 =", a2)
print()

# 3. 
suma = a1 + a2
print("3. Suma a1 i a2:", suma)

# 4.
roznica = a1 - a2
print("4. Różnica a1 - a2:", roznica)

# 5. 
print("5. Porównania:")
print("Czy a1 == a2?", a1 == a2)
print("Czy a1 != a2?", a1 != a2)
print("Czy a1 > a2?", a1 > a2)
print("Czy a1 < a2?", a1 < a2)
print()

# 6.
obie_wieksze_od_50 = a1 > 50 and a2 > 50
tylko_jedna_wieksza_od_50 = (a1 > 50) != (a2 > 50)

print("6. Liczby większe od 50:")
print("Czy obie są większe od 50?", obie_wieksze_od_50)
print("Czy tylko jedna jest większa od 50?", tylko_jedna_wieksza_od_50)
print()

# 7. 
tekst = "Fotogrametria"

czy_jest_o_z_kreska = "ó" in tekst
czy_jest_z_z_kropka = "ż" in tekst

print("7. Sprawdzenie liter w tekście:")
print("Tekst:", tekst)
print("Czy jest litera 'ó'?", czy_jest_o_z_kreska)
print("Czy jest litera 'ż'?", czy_jest_z_z_kropka)
print()

# 8. 
a = 6.3
pole = (a ** 2 * math.sqrt(3)) / 4

print("8. Pole trójkąta równobocznego dla a = 6.3:")
print("Pole =", pole)