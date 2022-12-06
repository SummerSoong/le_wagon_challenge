# A for Rock, B for Paper, and C for Scissors
opponent_transfer = {
    'A': 'Rock',
    'B': 'Paper',
    'C': 'Scissors'
}
# X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.
me_transfer = {
    "X": "lose",
    "Y": "draw",
    "Z": "win"
}
# 1 for Rock, 2 for Paper, and 3 for Scissors
point = {
    "Rock": 1,
    "Paper": 2,
    "Scissors": 3
}

def check_me(opponent, result):
    if opponent == "Rock":
        if result == "win":
            return "Paper"
        elif result == "lose":
            return "Scissors"
        else:
            return "Rock"
    if opponent == "Paper":
        if result == "win":
            return "Scissors"
        elif result == "lose":
            return "Rock"
        else:
            return "Paper"
    if opponent == "Scissors":
        if result == "win":
            return "Rock"
        elif result == "lose":
            return "Paper"
        else:
            return "Scissors"

def outcome_of_round(opponent, me):
    # 0 if you lost, 3 if the round was a draw, and 6 if you won
    if me == "Rock":
        if opponent == "Rock":
            return 3
        elif opponent == "Paper":
            return 0
        else:
            return 6
    if me == "Paper":
        if opponent == "Rock":
            return 6
        elif opponent == "Paper":
            return 3
        else:
            return 0
    if me == "Scissors":
        if opponent == "Rock":
            return 0
        elif opponent == "Paper":
            return 6
        else:
            return 3

with open('input.txt') as my_input:
    points = []
    for i, line in enumerate(my_input):
        # if i <= 10:
            opponent_mark = line.split()[0]
            opponent = opponent_transfer[opponent_mark]
            # print(f"opponent: {opponent}")
            result = me_transfer[line.split()[1]]
            me = check_me(opponent,result)
            # print(f"me: {me}")
            # print(f"point: {point[me]}")
            # print(f"outcome: {outcome_of_round(opponent, me)}")
            my_point = point[me] + outcome_of_round(opponent, me)
            points.append(my_point)
# print(points)
print(sum(points))
