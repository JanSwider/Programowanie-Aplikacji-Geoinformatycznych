import math
import random

# liczba pi
pi = math.pi
print("Pi:", pi)

# stopnie -> radiany
rad45 = math.radians(45)
rad90 = math.radians(90)
rad180 = math.radians(180)

print("Radiany:", rad45, rad90, rad180)

# radiany -> stopnie
deg45 = math.degrees(rad45)
deg90 = math.degrees(rad90)
deg180 = math.degrees(rad180)

print("Stopnie:", deg45, deg90, deg180)

# typy
print(type(rad45), type(deg45))

# logarytm
print("Log(54):", math.log(54))

# pierwiastek
print("sqrt(728):", math.sqrt(728))

# random
print("random():", random.random())
print("randint:", random.randint(1, 10))