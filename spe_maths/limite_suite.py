if __name__ == "__main__":
    n = 0
    u = 3+(-0.5)**n
    while u <= 2.999 or u >= 3.001 :
        n += 1
        u = 3+(-0.5)**n
    print(n)