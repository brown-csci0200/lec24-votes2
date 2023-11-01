
def cast_vote(poll, option_picked: str):
    if option_picked not in poll["options"]:
        raise ValueError("Invalid option")

    poll["votes"].append(option_picked)

def total_votes(poll):
    return len(poll["votes"])

def count_votes_for(poll, for_option):
    total = 0

    for v in poll["votes"]:
        if v == for_option:
            total += 1

    return total

some_poll = {
    "name": "what is your favorite color?",
    "options": ["red", "green", "blue"],
    "votes": [],
}

cast_vote(some_poll, "red")
cast_vote(some_poll, "green")
print(total_votes(some_poll))
