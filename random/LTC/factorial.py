##### DON'T TOUCH
tests :list[tuple[int, int]] = [
    (5, 120),
    (2, 2),
    (1, 1),
    (10, 3628800),
    (0, 1)
]

def test(function) -> None :
    for test in tests :
        print(
            f"{test[0]}! == {function(test[0])} :",
            "✅" if function(test[0]) == test[1]
            else "❌"
        )
#####
        
def factorial(num :int) -> int:
    # Your code here
    return 0

##### DONT'T TOUCH
if __name__ == "__main__" :
    test(factorial)