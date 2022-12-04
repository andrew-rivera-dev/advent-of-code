import fileinput

winningMove = {
    "A": "B",
    "B": "C",
    "C": "A"
}

losingMove = {
    "A": "C",
    "B": "A",
    "C": "B"
}

bonus = {
    "A": 1,
    "B": 2,
    "C": 3
}

def moveToPlay(opp, strategy):
    if strategy == "X":
        return losingMove[opp]
    elif strategy == "Y":
        return opp
    else:
        return winningMove[opp]

def calculateScore(moveWithStrategy):
    [move, strategy] = moveWithStrategy
    score = 0

    if strategy == "Y":
        score = 3
    elif strategy == "Z":
        score = 6
    
    return score + bonus[moveToPlay(move, strategy)]
    
score = 0

for line in fileinput.input(files ='2022/day2-data.txt'):
    moveWithStrategy = line.rstrip().split(" ")
    score += calculateScore(moveWithStrategy)

print(score)
