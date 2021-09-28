if __name__ == "__main__":
    n: int = 0
    u: float = 3+(-0.5)**n
    while u <= 2.999 or u >= 3.001 :
        n += 1
        u = 3+(-0.5)**n
    print(n)