first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
i=()
# Intersection is {57, 83, 29}
# First Set after removing common element
# {65, 42, 78, 23}
print(first_set.intersection(second_set))
n = first_set - second_set
print(n)