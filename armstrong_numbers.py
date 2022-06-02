'''Program to determine if a number is an armstrong number or not'''
def is_armstrong_number(number):
    x =  [int(a) for a in str(number)]
    n = len(x)
    c = []
    for a in x:
       b = a**n
       c.append(b)
    if sum(c) == number:
        return True
    return False
    '''Other way to do it'''
    return sum(a**n for a in x) == number#this line replace all below c=[]


if __name__=='__main__':
    print(is_armstrong_number(number=int(input('Favor ingresa un numero\n'))))
