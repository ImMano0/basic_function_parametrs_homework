# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.
def calculate_sum(suma):
    f = 0 
    a = 0 

    while f < len(suma):
        if suma[f] in (a, e, i, o, u, A, E, I, O, U):
             s += 1
        f += 1

    return s


print(calculate_sum(suma = "Hello World!"))