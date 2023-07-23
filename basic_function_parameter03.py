# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.
def find_smallest(smal):
    f = 1
    m = smal[0]
    while f < len(smal):
        if m > smal[f]:
            m = smal[f]
        f+=1
    return m
print(find_smallest(smal=[4,7,3,9,8,2,6,5]))