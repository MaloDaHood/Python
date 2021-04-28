import random
ng=1
while ng==1:
    print("Bienvenue sur le jeux des nombres secrets.\nVous devez deviner un nombre entre 100 et 999.")
    print("Tapez '0' si vous voulez arrêter le jeu.")
    essais=0
    nb=random.randint(100,999)
    rp=int(input("Votre premier essai ?\n"))
    essais+=1
    while rp!=nb:
        if rp==0:
            print("Arrêt du jeu.")
            quit()
        else:
            print("Mauvaise réponse !")
            if rp<nb:
                print("C'est plus !")
            elif rp>nb:
                print("C'est moins !")
            print("Vous avez fais", essais, "essais.")
            rp=int(input("Réessayez :\n"))
            essais+=1
    print("Bravo !\nC'était bien", nb)
    print("En tout vous avez fait", essais, "essais.")
    qng=input("Voulez-vous rejouer ? ('oui'/'non')\n")
    if qng=="oui":
        ng=1
    elif qng=="non":
        quit()
    else:
        print("Il fallait répondre 'oui' ou 'non'...")
        quit()
