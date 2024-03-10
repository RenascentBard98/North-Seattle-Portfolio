# Evan Wallace
# CSC 110
# 11/01/2023
# Matchmaking program to evaluate if two individuals are compatible based on a variety of factors


import math

# CONSTANTS

ATHLETICISM = 0.15
FOOD_OUT = 0.1
ENTERTAINMENT = 0.15
SERIOUSNESS = 0.2
RELIGION = 0.2
POLITICS = 0.2

def main():
# athletic = a, foodOut = f, entertainmentOut = e, seriousRelationship = s
# religious = r, religion = specific religion
# politics = p, political leaning = l
#              a  f   e  s  r    religion   p  l
    person1 = (7, 10, 6, 8, 10, "Judaism",  6, 8)
    person2 = (4, 5 , 6, 10, 8, "Atheist",  3, 2)
    matched = match(person1,person2)
    formattedMatch = format(matched * 100,'.1f')
    print('Match Probability: ', formattedMatch,"%")
    
# Matchmakes based of probability from rating function below

def match(person1, person2):
   # global ATHLETICISM, FOOD_OUT, ENTERTAINMENT, SERIOUSNESS, RELIGION, POLITICS
    # variables set equal to the positional values in the tuples
    a1, f1, e1, s1, r1, r11, p1, l1 = person1
    a2, f2, e2, s2, r2, r22, p2, l2 = person2

    athleteProb = rate(a1, a2) * ATHLETICISM
    foodProb    = rate(f1, f2) * FOOD_OUT
    entertainProb = rate(e1, e2) * ENTERTAINMENT
    monogamyProb = rate(s1, s2) * SERIOUSNESS
    
    #Religon Logic:
    if r1 >= 8 or r2 >= 8:
        if r11 == r22:
            religonProb = 1.0 * RELIGION
        else:
            religonProb = 0.5 * RELIGION
    else:
        religonProb = rate(r1, r2) * RELIGION

    #Politics Logic:
    if p1 >= 9 or p2 >= 9:
         politicsProb = rate(l1,l2) * POLITICS
    else:
         politicsProb = rate(p1, p2) * POLITICS

    finalMatch = athleteProb + foodProb + entertainProb + monogamyProb + religonProb + politicsProb
    return finalMatch

# Contains logic for "normal rating scale". Returns probability.

def rate(rating1, rating2):
    ratingDiff = abs(rating1 - rating2)
    matchProb = 0
    if ratingDiff == 0:
        matchProb = 1.0

    elif ratingDiff <= 1:
        matchProb = 1.0

    elif ratingDiff <= 3:
        matchProb = 0.7

    elif ratingDiff <= 6:
        matchProb = 0.4

    else:
        matchProb = 0

    return matchProb 

main()








