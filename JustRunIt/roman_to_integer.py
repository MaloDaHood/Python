##### DON'T TOUCH
tests :list[tuple[str, int]] = [
    ("III", 3),
    ("LVIII", 58),
    ("MCMXCIV", 1994),
    ("MMXXII", 2022),
    ("CDXX", 420)
]

def test(function) -> None :
    for test in tests :
        print(
            f"roman_to_integer(\"{test[0]}\") == {function(test[0])} :",
            "✅" if function(test[0]) == test[1]
            else "❌"
        )
#####        

def roman_to_integer(s :str) -> str :
    # Your code here
    return ""

##### DON'T TOUCH
if __name__ == "__main__" :
    test(roman_to_integer)