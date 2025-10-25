y = int(input("Ingrese un año entre 1800 y 2001: "))
a = round(y%19) #Hallar el residuo de Y dividido 19 y almacenarlo en a.
b = round(y/100) #Hallar el cociente de la división.
c = round(y%100) # Hallar el residuo de la división.
d = round(b/4)
e = round(b%4)
g = round((8*b+13) / 25)
h = round((((19*a)+b-d-g)+15)%30)
j = round(c/4)
k = round(c%4)
m = round((a+(11*h))/319)
r = round(((2*e)+(2*j)-k-h+m+32)%7)
n = round((h-m+r+90)/25)
p = round((h-m+r+19)%32)

print("La fecha de pascua fue en el día ", p,"en el mes ",n)

print("Revision de resultados: ")

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(j)
print(k)
print(m)
print(r)
print(n)
print(p)
