import random

def game():
    secret_number = random.randint(1, 100)
    guess = int(input("Make a guess : "))
    turns = 0
    
    while guess != secret_number:
        
        if guess > secret_number:
            print("Too high!")
        else:
            print("Too low!")
            
        guess = int(input("Make a guess : "))
        turns += 1
        
    print(f"You found it !\nIt was {secret_number}.\nIt took {turns} turns.")
    
if __name__ == "__main__":
    game()