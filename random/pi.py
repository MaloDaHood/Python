import time

if __name__ == "__main__" :
    x = 1
    pi = 4/x
    it = int(input("Combien d'itérations ?\n> "))
    start = time.time()
    for i in range(it) :
        x+=2
        if i % 2 == 0 :
            pi -= 4/x
        else :
            pi += 4/x
    print(f"Pi = {pi}")
    end = time.time()
    temps = end - start
    print(f"Temps d'éxécution : {temps:.3}ms")