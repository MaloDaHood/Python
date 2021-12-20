##### DON'T TOUCH
tests :list[tuple[list[int], int, list[int]]] = [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1]),
    ([98, 29, 43, 8, 34, 40, 32], 69, [1, 5]),
    ([68, 30, 67, -4], 26, [1, 3])
]

def test(function) -> None :
    for test in tests :
        print(
            f"twoSum({test[0]}, {test[1]}) == {function(test[0], test[1])} :",
            "✅" if function(test[0], test[1]) == test[2] or function(test[0], test[1]) == test[2][::-1]
            else "❌"
        )
#####

def twoSum(nums :list[int], target :int) -> list[int] :
    # Your code here
    return [-1, -1]

##### DON'T TOUCH
if __name__ == "__main__" :
    test(twoSum)