def reverse_string(string):
    reversed_string = ""
    for number in range(len(string) - 1, -1, -1):
        reversed_string += string[number]
    return reversed_string

def reverse_string_method(string):
    return "".join(reversed(string))

word = input("Mot : ")
print(reverse_string(word))
print(reverse_string_method(word))