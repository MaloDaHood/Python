import math
print("Calcul IMC")
p = int(input("Quel est votre poid en Kg ?"))
t = int(input("Quel est votre taille en centimètres ?"))
x = t/100
imc = p/x**2
print("Votre IMC est de :",round(imc,1))
if round(imc,1) < 18.5:
    print("Vous êtes en insuffisance pondérale.")
else:
    if round(imc,1) < 25:
        print("Vous avez une corpulence normale.")
    else:
        if round(imc,1) < 30:
            print("Vous êtes en surpoids.")
        else:
            if round(imc,1) < 35:
                print("Vous êtes en obésité modérée.")
            else:
                if round(imc,1) < 40:
                    print("Vous êtes en obésité sévère.")
                else:
                    if round(imc,1) > 40:
                        print("Vous êtes en obésité morbide ou massive.")