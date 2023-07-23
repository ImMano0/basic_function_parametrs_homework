# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.
def calculate_sum(suma):
    f = 0 
    a = 0 
    while f < len(suma):
        a += suma[f]
        f += 1 

    return a/len(suma) 

print(calculate_sum(suma=[3,4,6,8]))