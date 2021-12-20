##### DON'T TOUCH
tests :list[tuple[str, str]] = [
    ("hello", "olleh"),
    ("kayak", "kayak"),
    ("z", "z"),
    ("PyThOn", "nOhTyP"),
    ("12345", "54321")
]

def test(function) -> None :
    for test in tests :
        print(
            f"{test[0]} == {function(test[0])} :",
            "✅" if function(test[0]) == test[1]
            else "❌"
        )
#####

def reverse_str(string :str) -> str :
    # Your code here
    return ""

##### DON'T TOUCH
if __name__ == "__main__" :
    test(reverse_str)