
# Find the most voted person
# In case of a tie, bring the one with first letter in alphabet

# Obama         - 73 votes
# Trump         - 70 votes
# Peña beb￿é     - 150 votes
# Maduro        - 1 vote
# Zapata        - 150 votes
# AMLO          - 0 votes

#VOTING_SYSTEM
def get_most_voted():

    votes = {'Obama':73, 'Trump':70, 'Peña bb':150, 'Maduro':1, 'Zapata':150, 'AMLO':0, 'Angel':150}

    most_voted = []
    total_votes = 0

    for key, value in votes.items():
        if value > total_votes:
            total_votes = value
        if votes[key] >= total_votes:
            most_voted.append(key.lower())

    if len(most_voted) > 1:
        most_voted.append(min(most_voted))


    print(max(votes))
    print(total_votes)
    print("The winner is: " + most_voted[-1].capitalize())

get_most_voted()
