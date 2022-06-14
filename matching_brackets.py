'''Program to validate matching brackets'''
def validate(text):
    '''Param: str - Introduced by user
       return: bool -  True if matching brackets False if not
    '''
    A = ('(',')','[',']','{','}')
    a = [0]
    for i in text:
        if i in A:
            b = A.index(i)
            if b % 2 == 0:
                a.append(i)
            else:
                if a[-1] != A[b-1]:
                    return False
                a.pop()
    return  a == [0]

if __name__=='__main__':
    text =  str(input('Ingrese un texto\n'))
    print(validate(text))
