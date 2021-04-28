import time, random
c1=random.randint(2, 11)
c2=random.randint(2, 11)
cT1=c1+c2
cT=cT1
ls=["oui", "non"]
print("Vous tirez un", c1, "et un", c2, "\nVous êtes à", cT1)
if cT1>21:
    print("Vous perdez !")
    quit()
elif cT1==21:
    print("Vous gagnez !")
    quit()
ans=input("Voulez-vous continuer ? (oui/non)\n")
if ans=="oui": #CONTINUE ("OUI")
    x=0
    while ans=="oui": #########INCOMPLET#########
        x1=x
        x=random.randint(2, 11)
        cT2=cT1+x1+x
        cT=cT2
        time.sleep(0.5)
        print("Vous tirez un", x, "\nVous êtes à", cT2)
        if cT2 > 21:
            print("Vous perdez !")
            quit()
        elif cT2==21:
            print("Vous gagnez !")
            quit()
        ans=input("Voulez-vous continuer ? (oui/non)\n")
        if ans in ls:
            pass
        else: #NI "OUI" NI "NON"
            print("Vous devez répondre par 'oui' ou 'non' !")
            time.sleep(1)
            print("On recommence...")
            quit()
    else: #CONTINUE PAS ("NON")
        non=1
elif ans=="non": #CONTINUE PAS ("NON")
    non=1
else: #NI "OUI" NI "NON"
    print("Vous devez répondre par 'oui' ou 'non' !")
    time.sleep(1)
    print("On recommence...")
    quit()
if non==1: #REPONSE = "NON"
    cC1=random.randint(2, 11)
    cC2=random.randint(2, 11)
    cCT1=cC1+cC2
    cCT=cCT1
    print("Le croupier tire un", cC1, "et un", cC2, "\nLe croupier est à", cCT1)
    if cCT1>21:
        print("Le croupier perd, vous gagnez !")
        quit()
    elif cCT1==21:
        print("Le croupier gagne, vous perdez.")
        quit()
    elif cCT1<=15:
        cC3=random.randint(2, 11)
        cCT2=cCT1+cC3
        cCT=cCT2
        time.sleep(1)
        print("Le croupier pioche une autre carte. \nC'est un", cC3, "\nIl est à", cCT2)
        if cCT2>21:
            print("Le croupier perd, vous gagnez !")
            quit()
        elif cCT2==21:
            print("Le croupier gagne, vous perdez.")
            quit()
cPF=21-cT
cCF=21-cCT
time.sleep(1)
print("---------------------------------------------------")
if cPF<cCF:
    print("Vous gagnez avec", cT, "\nLe croupier avait", cCT, "\nBravo !")
    quit()
elif cCF<cPF:
    print("Vous perdez avec", cT, "\nLe croupier gagne avec", cCT)
    quit()
elif cPF==cCF:
    print("Egalité ! \nLe croupier et vous êtes à", cT)