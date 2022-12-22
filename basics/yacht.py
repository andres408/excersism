'''Program to evaluate dices according to yacht categories'''
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL HOUSE'
FOUR_OF_A_KIND = 'Four of a kind'
LITTLE_STRAIGHT = 'LITTLE STRAIGH'
BIG_STRAIGHT = 'BIG STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    '''Param: int five numbers in the dice
       return: int Score according to category
    '''
    n=0
    counter=0
    dice =sorted(dice)
    '''if category == ONES or category == TWOS or category == THREES or category == FOURS or category==FIVES or category==SIXES:
        n = [x for x in dice if x == category]
        for x in n:
            counter +=1
        return counter*category'''

    if category == CHOICE:
        return sum(dice)

    if category ==  FULL_HOUSE:
        if (len(set(dice)))==2:#Valido si la lista tiene dos valores 
            a = [x for x in dice if x ==  (sorted(dice)[0])]#Organizo la lista y comparo todos los valores  con el primer indice para hacer la primera nueva lista
            b = [x for x in dice if x == (sorted(dice)[-1])]#Organizo la lista y comparo todos los valores con el ultimo indice para hacer la segunda nueva lista
        else:
            return 0
    
        if (len(a) == 3 and len(b)==2) or (len(a) == 2 and len(b)==3):
            return sum(dice)
        return 0
    
    if category == FOUR_OF_A_KIND:
        c = []
        d = []
        if (len(set(dice)))==2:
            c = [x for x in dice if x == dice[0]]
            d = [x for x in dice if x == dice[-1]]
            if len(c) == 4:
                return sum(c)
            if len(d) == 4:
                return sum(d)
            return 0
        if (len(set(dice)))==1:
            return sum(dice[0:4])
        return 0
        
    if category == LITTLE_STRAIGHT:
        if (len(set(dice)))==5 and 6 not in dice:
            return 30
        return 0
        
    if category == BIG_STRAIGHT:
        if (len(set(dice)))==5 and 1 not in dice:
            return 30
        return 0

        


if __name__=='__main__':
    print(score(dice = [2,6,3,4,5],category=BIG_STRAIGHT))
