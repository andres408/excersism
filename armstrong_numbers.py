'''Program to determine if a number is an armstrong number or not'''
import time
time1 = 0
time2 = 0
time3 = 0
def is_armstrong_number(number):
    x =  [int(a) for a in str(number)]
    n = len(x)
    c = []
    return sum(a ** len(x) for a in x) == number
    ''' for a in x:
       b = a**n
       c.append(b)
    if sum(c) == number:
        return True
    return False
    '''
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

def _get_digits(number: int) -> list[int]:
    digits = []
    while number:
        digit = number % 10
        digits.append(digit)
        number //= 10
    return digits

def is_armstrong_number2(number):
    digits = _get_digits(number)
    return sum(a ** len(digits) for a in digits) == number

def is_armstrong_number3(number):
    digits = []
    c = number
    while c:
        digit = c % 10
        digits.append(digit)
        c //= 10
    return sum(a ** len(digits) for a in digits) == number

if __name__=='__main__':
    number =  int(input('Please introduce a number\n'))
    start = time.time()
    print(is_armstrong_number(number))
    end = time.time()
    start1= time.time()
    print(is_armstrong_number1(number))
    end1 = time.time()
    start2 = time.time()
    print(is_armstrong_number2(number))
    end2 = time.time()
    start3 = time.time()
    print(is_armstrong_number3(number))
    end3 = time.time()

time1 = end - start
time2 = end1 - start1
time3 = end2 - start2
time4 = end3 - start3
print('Algoritmo uno toma: ', time1)
print('Algoritmo dos toma: ', time2)
print('Algoritmo 3   toma: ', time3)
print('Algoritmo 4   toma: ', time4)
