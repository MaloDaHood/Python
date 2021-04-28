import math, random, time
print("Bienvenue sur cette partie de bataille.")
time.sleep(2)
ScoreMax = int(input("Quel est le score maximal ?"))
ScoreP1 = 0
ScoreP2 = 0
while True:
    CarteP1 = random.randint(2,14)
    CarteP2 = random.randint(2,14)
    print("P1 a",CarteP1,"et P2 a",CarteP2)
    if CarteP1 > CarteP2:
        ScoreP1+=1
        print("P1 gagne !")
        print("P1 :",ScoreP1,"points et P2 :",ScoreP2,"points")
    if CarteP2 > CarteP1:
        ScoreP2+=1
        print("P2 gagne !")
        print("P1 :",ScoreP1,"points et P2 :",ScoreP2,"points")
    if CarteP1 == CarteP2:
        print("égalité")
    if ScoreP1 == ScoreMax:
        print("P1 a gagné !")
        break
    if ScoreP2 == ScoreMax:
        print("P2 a gagné !")
        break
    time.sleep(5)