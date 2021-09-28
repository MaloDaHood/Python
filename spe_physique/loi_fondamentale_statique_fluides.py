r = 1
g = 6.67e-11
Za = float(input("Quelle est l'altitude de A ?"))
Zb = float(input("Quelle est l'altitude de B ?"))
D = r*g*(Zb-Za)
print("La différence de pression entre A et B est de ", D)