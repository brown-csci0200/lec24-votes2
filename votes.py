x = 5 + 3

x += 10

print(x)
print(x + 1)

# Variables are in snake_case
some_string = "string"

# List with 3 things
option_list = ["red", "green", "blue"]
print(option_list)


# defines a function
# Note:  in Python:  indentation defines the structure of the code
# Optionally:  can add "type annotations" to code.  Python may be able to give warnings if you do this
def some_function(a: int) -> bool: 
    if a < 5:
        print("less than 5")
        print("yay")
        return True
    elif a > 10:
        print("greater than 10")
        return False
    else:
        print("bbooooo")
        return False



some_function(2)

# In python, type checking only happens as the code runs
# We don't notice this is an error until the previous code runs
#some_function("some string")

# If you have strong feelings about this, take CS173

# How to set up a class
class PollRecord:
        
    # Define fields and set them up
    # __init__ is the name for a constructor
    # "self" refers to the current object (like "this")
    # Needs to be the first argument of any method
    def __init__(self, name: str, options: list[str]):
        self.name = name      # Set up a field, assign a value to it
        self.options = options
        self.votes = list()   # Make a new field with an empty list

    def cast_vote(self, for_option):
        if for_option in self.options:   # is for_option contained in self.options
            self.votes.append(for_option)
        else:
            raise ValueError("Wrong option " + for_option)
        
    def count_votes_for(self, for_option: str) -> int:
        total = 0

        # "for each loop"
        # for v in self.votes:
        #     if v == for_option:
        #         total += 1

        # Loop over array by index
        # len(x) == size of x (length of array, length of string)
        for i in range(0, len(self.votes)):
            v = self.votes[i]  #Look up item in list
            if v == for_option:
                total += 1

        return total


option_list = ["red", "green", "blue"]
p = PollRecord("What is your favorite color?", option_list)
p.cast_vote("red")
p.cast_vote("green")

print("Green has " + str(p.count_votes_for("green")) + " votes")

# To see what your python code is doing
# 1. Add pass statement where you want to stop
pass # BLank statement, does nothing

