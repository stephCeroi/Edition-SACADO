p = int(input("Quelle précision ?"))
a = int(input("De quel nombre souhaitez vous la racine carrée ?"))
precision = 10**(-p)
v = -a
i=0
while v < 0 :
    v= i**2 - a
    if v >0:
        print(i-precision ,"<= a <=", i)
        break
    i=i+precision
