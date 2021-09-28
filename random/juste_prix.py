import random

def random_number(max: int) -> int :
    return random.randint(1, max)

def is_number(num: int, secret_number: int) -> bool :
    return num == secret_number

def compare(num: int, secret_number: int) -> str :
    if num < secret_number :
        return "more"
    else :
        return "less"
    
def play_again() -> bool :
    while True :
        try :
            choice: int = int(input("Do you want to play again ?\n1. YES\n2. NO\n> "))
            if choice < 1 or choice > 2 :
                print("You have to input either '1' or '2'.")
            else :
                break
        except ValueError :
            print("You have to input an integer.")
    if choice == 1 :
        return True
    else :
        return False

if __name__ == "__main__" :
    playing: bool = True
    while playing :
        print("The computer chooses a random integer and you have to guess it.")
        while True :
            try :
                max_value: int = int(input("Please choose the maximum value the integer can be. (must be at least 2)\n> "))
                if max_value <= 1 :
                    print("The value can't be 1 or less.")
                else :
                    break
            except ValueError :
                print("You have to input an integer.")
        secret_number: int = random_number(max_value)
        num: int = 0
        number_of_turns: int = 0
        while not is_number(num, secret_number) :
            while True :
                try :
                    num = int(input("Make a guess > "))
                    if num < 1 or num > max_value :
                        print(f"Your guess has to be between 1 and {max_value}. (both included)")
                    else :
                        break
                except ValueError :
                    print("You have to input an integer.")
            number_of_turns += 1
            if is_number(num, secret_number) :
                break
            else :
                print(f"It is {compare(num, secret_number)}")
        print(f"Congratulations you found the secret number, it was {secret_number} !")
        print(f"You found it in {number_of_turns} turns.")
        playing = play_again()