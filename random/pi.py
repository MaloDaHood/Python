import time

if __name__ == "__main__" :
    x: int = 1
    pi: float = 4/x
    it: int = int(input("Combien d'itérations ?\n> "))
    start: float = time.time()
    for i in range(it) :
        x += 2
        if i % 2 == 0 :
            pi -= 4/x
        else :
            pi += 4/x
    print(f"Pi = {pi}")
    end: float = time.time()
    temps: float = end - start
    print(f"Temps d'éxécution : {temps:.3}ms")