import random

MIN = 1
MAX = 20
QUESTIONS = 30

def question(i):
    func = [add, sous, mult, div]
    while len(func) < QUESTIONS :
        func_copy = func.copy()
        for obj in func_copy:
            func.append(obj)
    if func[i](random.randint(MIN, MAX), random.randint(MIN, MAX)):
        print("Bonne réponse")
    else:
        print("Mauvaise réponse")

def add(a, b):
    return int(input(f"{a}+{b} = ")) == a+b

def sous(a, b):
    return int(input(f"{a}-{b} = ")) == a-b

def mult(a, b):
    return int(input(f"{a}*{b} = ")) == a*b

def div(a, b):
    return float(input(f"{a}/{b} = ")) == a/b

if __name__ == "__main__":
    for i in range(QUESTIONS):
        print(f"Question n° {i+1}/{QUESTIONS} :")
        question(i)