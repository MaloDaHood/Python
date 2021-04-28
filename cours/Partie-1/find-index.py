chaine="Bonjour le jour"
print(chaine.find("jour"))  #renvoie la position du premier caractère 
                            #de la première occurence
                            #renvoie -1 si rien n'est trouvé

print(chaine.index("jour")) #pareil mais renvoie une erreur si rien n'est trouvé

print(chaine.rfind("jour")) #pareil que .find() mais pars de la droite