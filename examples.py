some_votes = ["red", "red", "green"]

# Another way to iterate
def count_votes(votes, for_option):
    for i in range(0, len(votes)):
        v = votes[i]  #Look up item in list by index
        if v == for_option:
            total += 1

    return total

###################################
# Have this
ex1 = ["8", "10", "-5.5"]

# Want:  [8, 10, 5.5]

###################################
# Have this
ex2 = ["hello", "WORLD", "pYthon"]

# Want:  ["hello", "world", "python"]


###################################
# Have this:
ex3 = [0, 5, -2, -4, 7]

# Want: [5, 7]


###################################
# Have this:
ex4 = ["pvd", "boston", "wos", "newport"]

# Want:  ["PVD", "WOS"]

###################################
# Indexes:     0  1  2  3  4  5
ex5 =         [8, 3, 5, 9, 0, 2]

# Want:  [0, 4, 5] (Indices of numbers in list that are even)


