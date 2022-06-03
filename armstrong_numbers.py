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

def is_armstrong_number1(number):
    digits = 0
    a = number
    b = number
    suma = 0
    while(a>0):
        a =  a//10
        digits +=1
    while(b>0):
        suma += (b%10)**digits
        b = b //10
    
    return suma == number

if __name__=='__main__':
    number =  int(input('Please introduce a number\n'))
    print(is_armstrong_number(number))
    print(is_armstrong_number1(number))
