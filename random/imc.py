import math
print("Calcul IMC")
p: int = int(input("Quel est votre poids en Kg ?"))
t: int = int(input("Quel est votre taille en centimètres ?"))
x: float = t/100
imc: float = p/x**2
print("Votre IMC est de :",round(imc,1))
if round(imc,1) < 18.5:
    print("Vous êtes en insuffisance pondérale.")
elif round(imc,1) < 25:
    print("Vous avez une corpulence normale.")
elif round(imc,1) < 30:
    print("Vous êtes en surpoids.")
elif round(imc,1) < 35:
    print("Vous êtes en obésité modérée.")
elif round(imc,1) < 40:
    print("Vous êtes en obésité sévère.")
else:
    print("Vous êtes en obésité morbide ou massive.")