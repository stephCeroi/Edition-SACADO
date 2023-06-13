a=int(input("Entrer un nombre " ))
b=int(input("Entrer un nombre " ))
r=a%b

while  b!=0:
    r=a%b
    a,b=b,r

print(a)

