tab = []
ok = True

while ok :
    v  = float(input("Entrer une valeur numerique."))
    tab.append(v)
    rep = input("Souhaitez-vous continuer ? O/N")
    if rep=="N":
        ok=False
print(tab)