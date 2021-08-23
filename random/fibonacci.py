if __name__ == "__main__" :
    a = 0
    b = 1
    for i in range(10) :
        x = a + b
        a = b
        b = x
        print(x)