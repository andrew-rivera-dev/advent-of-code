import fileinput

def convertMove(xyz):
    if xyz == "X":
        return "A"
    if xyz == "Y":
        return "B"
    return "C"

def calculateScore(moveSet):
    [opp, me] = moveSet
    score = 0
    if opp == me:
        score = 3
    
    match opp:
        case "A":
            if me == "B":
                score = 6
        case "B":
            if me == "C":
                score = 6
        case "C":
            if me == "A":
                score = 6
    
    return score + calculateBonus(me)

def calculateBonus(move):
    if move == "A":
        return 1
    elif move == "B":
        return 2
    return 3
    
score = 0

for line in fileinput.input(files ='2022-day2-data.txt'):
    moveSet = line.rstrip().split(" ")
    moveSet[1] = convertMove(moveSet[1])
    score += calculateScore(moveSet)

print(score)

