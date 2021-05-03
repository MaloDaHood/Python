### QCM 

def demander_si_personne_veut_jouer():
    qcm = input("Would you like to play a little MCQ ? (y/n) ")
    if qcm == "y" or qcm == "Y":
        game1 = ''
game_game = demander_si_personne_veut_jouer()


def game():
    question = input("""What's your favorit subject at school ? 
                                if it maths type(1)
                                if history type(2)
                                if physics type(3)
                                if computer science type(4)""")
    while int(question) == 1:
        answer = input("""Nice! 
                            What's Pythagore theorem?
                                                        (1) --> AB**2= AC**2 + BC**2
                                                        (2) --> BC = AC**2 + AB**2
                                                        (3) --> AB = AC * BC
                                                        
                                                        """)
        if int(answer) == 1:
            print("Congratulation you're a king !")
            play_again = input("End of the game do want to play again ? (y/n) ")
            if "y":
                game2 = game()
            else:
                break
        else:
            print("Nope wrong answer go back to your studies...")
            play_again = input("End of the game do want to play again ? (y/n) ")
            if "y":
                game2 = game()
            else:
                break
    
    while int(question) == 2:
        answer2 = input("""Nice!
                            When secession war ended? 
                                                        1 --> 1861
                                                        2 --> 1965
                                                        3 --> 1865
                                                        
                                                        """)
        if int(answer2) == 3:
            print("Congratulation you're a king !")
            play_again = input("End of the game do want to play again ? (y/n) ")
            if "y":
                game2 = game()
            else:
                break
        else:
            print("Nope wrong answer go back to your studies...")
            play_again = input("End of the game do want to play again ? (y/n) ")
            if "y":
                game2 = game()
            else:
                break

    while int(question) == 3: 
        answer3 = input("""Nice! 
                            What's thermodynamic ?
                                                        1 --> studies of cold and movements
                                                        2 --> the area of physics connected with the action of heat
                                                              and other types of energy
                                                        3 --> studies of elctro pulses
                                                        
                                                        """)
        if int(answer3) == 2:
            print("Congratulation you're a king !")
            play_again = input("End of the game do want to play again ? (y/n) ")
            if "y":
                game2 = game()
            else:
                break
        else:
            print("Nope wrong answer go back to your studies...")
            play_again = input("End of the game do want to play again ? (y/n) ")
            if "y":
                game2 = game()
            else:
                break

    while int(question) == 4:
        answer4 = input("""Nice! 
                            What are the computer languages for web pages ?
                                                        1 --> html and python
                                                        2 --> html and css
                                                        3 --> java
                                                        
                                                        """)
        if int(answer4) == 2:
            print("Congratulation you're a king !")
            play_again = input("End of the game do want to play again ? (y/n) ")
            if "y":
                game2 = game()
            else:
                break
        else:
            print("Nope wrong answer go back to your studies...")
            play_again = input("End of the game do want to play again ? (y/n) ")
            if "y":
                game2 = game()
            else:
                break
    return game

play_again = input("Are you ready ? (y/n) ")
if "y":
    game2 = game()