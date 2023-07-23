# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.
def calculate_sum(suma):
    f = 0 
    a = 0 
    while f < len(suma):
        a += suma[f]
        f += 1 

    return a 

print(calculate_sum(suma=[3,4,6,8]))