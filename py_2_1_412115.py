tekst = "A, wie pan, moim zdaniem to nie ma tak, że dobrze, albo że niedobrze. Gdybym miał powiedzieć, co cenię w życiu najbardziej, powiedziałbym, że ..."

# czy jest "-"
print("-" in tekst)

# ile przecinków
print(tekst.count(","))

# zamiana przecinków na kropki
tekst = tekst.replace(",", ".")

# dodanie po ...
tekst = tekst.replace("...", "... coś tam")

# nowa linia po kropce
tekst = tekst.replace(". ", ".\n")

print(tekst)