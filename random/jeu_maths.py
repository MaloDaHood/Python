import random

MIN: int = 1
MAX: int = 20
QUESTIONS: int = 30

def question(i) -> None :
    func: list = [add, sous, mult, div]
    while len(func) < QUESTIONS :
        func_copy: list = func.copy()
        for obj in func_copy:
            func.append(obj)
    if func[i](random.randint(MIN, MAX), random.randint(MIN, MAX)):
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")

def add(a: int, b: int) -> bool :
    return int(input(f"{a}+{b} = ")) == a+b

def sous(a: int, b: int) -> bool :
    return int(input(f"{a}-{b} = ")) == a-b

def mult(a: int, b: int) -> bool :
    return int(input(f"{a}*{b} = ")) == a*b

def div(a: int, b: int) -> bool :
    return float(input(f"{a}/{b} = ")) == a/b

if __name__ == "__main__":
    for i in range(QUESTIONS):
        print(f"Question n° {i+1}/{QUESTIONS} :")
        question(i)