import time, random
print("Calculateur de taille.")
t = int(input("Quelle est votre taille en centimètre ?"))
print("Calcul en cours ....")
time.sleep(random.randint(1,10))
print("Vous faites", t, "cm.")
if t < 160 :
    print("T'es vraiment po grand !")
    quit()
if t > 190 :
    print("T'es géant toi c'est un truc de ouf !")
if t > 220 : 
    print("En vrai, tu mens ?")
    quit()
else :
    quit()