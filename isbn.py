'''Program to evaluate if an ISBN number is correct'''
def valid(isbn):
    '''Param: str- string introduced by user
       return: bool - True is ISBN number is correct False otherwise'''
    if isbn:
        a = list(isbn.replace('-',''))
        b = 0
        c = 10
        for i in a:
            if a[-1].lower() == 'x':
                a[-1] = '10'
            if len(a)!= 10:
                return False
            if i.isnumeric():
                b += int(i) * c
                c-=1
            else:
                return False
        return b % 11 == 0
    else:
        return False
        
if __name__=='__main__':
    
    print(valid(isbn=input('ingrese el valor\n')))
