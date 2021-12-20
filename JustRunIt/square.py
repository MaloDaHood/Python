def square(width, height):
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print("\n", end="")
        
square(5, 5)

print("\n\n")

def triangle(value):
    for i in range(value):
        for j in range(i + 1):
            print("*", end="")
        print("\n", end="")
        
    for i in range(value, 0, -1):
        for j in range(i - 1, 0, -1):
            print("*", end="")
        print("\n", end="")
        
triangle(10)