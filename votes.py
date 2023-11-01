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
        
    def count_votes(self):
        return len(self.votes) # Get the length of most Python objects (string, list, dictionary, ...)
        
    def count_votes_for(self, for_option: str) -> int:
        total = 0

        # "for each loop"
        for v in self.votes:
            if v == for_option:
                total += 1

        return total
    
    # Like Java's toString
    def __str__(self) -> str:
        return "Poll for question " + self.name + ", choices:  " + str(self.options)


option_list = ["red", "green", "blue"]
p = PollRecord("What is your favorite color?", option_list)
print(p)
p.cast_vote("red")
p.cast_vote("green")

print("Green has " + str(p.count_votes_for("green")) + " votes")

# To see what your python code is doing
# 1. Add pass statement where you want to stop
pass # BLank statement, does nothing

