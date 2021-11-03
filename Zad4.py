KapitalPoczatkowy = int(input("Podaj kapitał początkowy: "))
MiesieczneWplywy = int(input("Podaj miesięczne wpływy: "))
OkresInwestowania = int(input("Podaj okres inwestowania w miesiącach: "))
WartoscInwestycji = int(input("Podaj pożądaną końcową wartość inwestycji: "))

wynik = (KapitalPoczatkowy + (MiesieczneWplywy * OkresInwestowania)) * 1.02

if wynik < WartoscInwestycji:
    print("Końcowa wartość inwestycji (" + str(wynik) + ") jest mnniejsza niż oczekiwana (" + str(WartoscInwestycji) + ")")
else:
    print("Końcowa wartość inwestycji (" + str(wynik) + ") jest większa niż oczekiwana (" + str(WartoscInwestycji) + ")")
        
