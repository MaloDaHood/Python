import math
print ("Programme pour obtenir le PGCD et le PPCM de deux nombres.")
print ("Test d'ajout de boucles.")
p = int(input("Premier nombre ?"))
k = int(input("Deuxième nombre ?"))
s = p
c = k
w = p%k
while w >> 0:
    p = k
    k = w
    w = p%k
    m = s*c/k
print ("PGCD =",(k))
print ("PPCM =",(m))
print ("Reste =",(w))
if k == 1:
    print ("Ils sont premiers entre eux !")
