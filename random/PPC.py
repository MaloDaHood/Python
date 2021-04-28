import random
ls=["p", "f", "c"]
pt=0
ptB=0
toursD=int(input("Combien de tours voulez-vous faire ?"))
tours=0
while tours<=toursD:
    mv=input("Que voulez-vous faire ? pierre/feuille/ciseau=('p'/'f'/'c')")
    if mv in (ls):
        pass
    else:
        print("Vous devez écrire 'p', 'f' ou 'c'.")
        quit()
    mvB=random.choice(ls)
    if mv==mvB:
        print("Egalité")
    elif mv=="p":
        print("Vous faites pierre.")
        if mvB=="f":
            print("L'ordinateur fait feuille.\nIl gagne.")
            ptB+=1
            print("1 point pour l'ordinateur.")
        elif mvB=="c":
            print("L'ordinateur fait ciseau.\nVous gagnez !")
            pt+=1
            print("1 point pour vous !")
    elif mv=="f":
        print("Vous faites feuille.")
        if mvB=="c":
            print("L'ordinateur fait ciseau.\nIl gagne.")
            ptB+=1
            print("1 point pour l'ordinateur.")
        elif mvB=="p":
            print("L'ordinateur fait pierre.\nVous gagnez !")
            pt+=1
            print("1 point pour vous !")
    elif mv=="c":
        print("Vous faites ciseau.")
        if mvB=="p":
            print("L'ordinateur fait pierre.\nIl gagne.")
            ptB+=1
            print("1 point pour l'ordinateur.")
        elif mvB=="f":
            print("L'ordinateur fait feuille.\nVous gagnez !")
            pt+=1
            print("1 point pour vous !")
    print("Votre Score :", pt)
    print("Score de l'ordinateur :", ptB)
    tours+=1
if pt==ptB:
    print("C'est fini ! \nIl y a égalité :", pt, "partout.")
    quit()
elif pt>ptB:
    print("Cest fini ! \nVous gagnez avec", pt, "points contre", ptB, "points pour l'ordinateur.")
    quit()
elif pt<ptB:
    print("Cest fini ! \nL'ordinateur gagne avec", pt, "points contre", ptB, "points pour vous.")
    quit()