
dice =[1,1,0,0,1]
YACHT = 50
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'FULL HOUSE'
FOUR_OF_A_KIND = 16
LITTLE_STRAIGHT = 30
BIG_STRAIGHT = 30
CHOICE = 'CHOICE'


def organizar(dice, category):
    n=0
    counter=0
    aa=[]
    bb=[]
    if category == ONES or category == TWOS or category == THREES or category == FOURS or category==FIVES or category==SIXES:
        n = [x for x in dice if x == category]
        for x in n:
            counter +=1
        return counter*category
    if category == CHOICE:
        return sum(dice)
    if category ==  FULL_HOUSE:
        if (len(set(dice)))==2:
            ''' a = sorted(dice)[0]
            b =  sorted(dice)[-1]'''
            c = [x for x in dice if x == (sorted(dice)[0])]
            d = [x for x in dice if x == (sorted(dice)[-1])]
            print(c,d)
            '''for x in dice:
                if x == a:
                    c.append(x)
                else:
                    d.append(x)
            print(c,d)'''
        else:
            return 0
               
        if (len(c) == 3 and len(d)==2) or (len(c) == 2 and len(d)==3):
            return sum(dice)
        return 0


if __name__=='__main__':
    print(organizar(dice,category=FULL_HOUSE))
