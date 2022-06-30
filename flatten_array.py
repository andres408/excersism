'''Program to clean a list'''
def flatten(iterable):
    '''Param: list - A list or nested lists.
       Return: list - One list only with values different to None'''
    a = []
    for i in iterable:
        if type(i) == list:
            a+=flatten(i)
        elif i != None:
            a.append(i)
    return a

if __name__=='__main__':
    iterable = [0,1,2,[[3,4]]]
    print(flatten(iterable))
