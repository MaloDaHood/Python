##### DON'T TOUCH
tests :list[str] = [
    "hello",
    "kayak",
    "z",
    "PyThOn",
    "12345"
]

def test(function) -> None :
    for test in tests :
        print(
            f"{test} == {function(test)} :",
            "✅" if function(test) == test[::-1]
            else "❌"
        )
#####

def reverse_str(string :str) -> str :
    # Your code here
    return ""

##### DON'T TOUCH
if __name__ == "__main__" :
    test(reverse_str)