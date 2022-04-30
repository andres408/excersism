'''Solution to sublist exercise'''
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one,list_two):
    one = str(list_one).strip("[]") + ","
    two = str(list_two).strip("[]") + ","
    if list_one == list_two:
        return EQUAL
    if one in two:
        return SUBLIST
    if two in one:
        return SUPERLIST
    return UNEQUAL

if __name__=='__main__':
    print(sublist(list_one=[5], list_two=[6]))
