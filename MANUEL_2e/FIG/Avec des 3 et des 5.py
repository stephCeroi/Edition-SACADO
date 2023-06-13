n=int(input("Entrer un prix à payer, supérieur ou égal à 8"))
for i in range(n//3+1):
    if (n-3*i)%5==0 :
        print(n,"peut se payer avec",int(i),"pièces de 3 et",int((n-3*i)/5),"pièces de 5")
