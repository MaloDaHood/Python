a=int(float(input("Nombre stoechiomètrique du réactif A :\n")))
b=int(float(input("Nombre stoechiomètrique du réactif B :\n")))
c=int(float(input("Nombre stoechiomètrique du produit C :\n")))
d=int(float(input("Nombre stoechiomètrique du produit D :\n")))
###############################################################
nI_a=float(input("Quantité matière initiale réactif A :\n"))
nI_b=float(input("Quantité matière initiale réactif B :\n"))
###############################################################
xmax1=nI_a/a
print("Si réactif A est limitant xmax = ", xmax1, "mol.")
xmax2=nI_b/b
print("Si réactif B est limitant xmax = ", xmax2, "mol.")
###############################################################
if xmax1<xmax2:
    xmax=xmax1
    lim="réactif A"
elif xmax1==xmax2:
    xmax=xmax1
    lim="les deux"
    print("Les conditions stoechiomètriques sont appliquées.")
else:
    xmax=xmax2
    lim="réactif B"
print("xmax a une valeur de ", xmax, "mol.\nLe réactif limitant est le ", lim)
###############################################################
nF_a=nI_a-a*xmax
print("Quantité matière état final réactif A = ", nF_a, "mol.")
nF_b=nI_b-b*xmax
print("Quantité matière état final réactif B = ", nF_b, "mol.")
nF_c=c*xmax
print("Quantité matière état final produit C = ", nF_c, "mol.")
nF_d=d*xmax
print("Quantité matière état final produit D = ", nF_d, "mol.")
