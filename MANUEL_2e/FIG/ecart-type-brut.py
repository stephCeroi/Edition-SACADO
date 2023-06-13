import math
tab = [1.,2.,3.5,5.,6.,7.,7.4,7.8,8.2,8.4,8.5,9.,10.2,12.5]

def tab_carre(tab):
    tab_carre = []
    for t in tab:
        c = t**2
        tab_carre.append(c)
    return tab_carre

def average(tab): ## Renvoi de la moyenne
    somme = 0
    for t in tab:
        somme += t
    avg = somme/len(tab)
    return avg


def std(tab): ## Renvoi de l'ecart-type
    var = average(tab_carre(tab))-average(tab)**2
    sigma = math.sqrt(var)
    return sigma

print("Ecart-type = ", std(tab))