##### DON'T TOUCH
tests :list[tuple[int, bool]] = [
    (121, True),
    (-121, False),
    (10, False),
    (56465, True),
    (98765432123456789, True)
]

def test(function) -> None :
    for test in tests :
        print(
            f"is_palindrome({test[0]}) == {function(test[0])} :",
            "✅" if function(test[0]) == test[1]
            else "❌"
        )
#####        
        
def is_palindrome(x :int) -> bool :
    # Your code here
    return True

##### DON'T TOUCH
if __name__ == "__main__" :
    test(is_palindrome)