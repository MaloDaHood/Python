import random

a=random.randint(0, 1)
print(a)

b=random.uniform(0, 1)
print(b)

c=random.randrange(0, 101, 10)
print(c)

import os, time

chemin="C:\\Users\\Malo\\Documents\\GitHub\\Python\\cours\\Partie-1" 
dossier=os.path.join(chemin, "dossier")
os.makedirs(dossier)
time.sleep(2)
if os.path.exists(dossier):
    os.removedirs(dossier)