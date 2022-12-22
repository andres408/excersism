'''Program to calculate difference from square of sum and sum of squares'''
def square_of_sum(number):
    '''Param: int -  number given by user
       Return: int - square of sum of numbers in number given'''
    n = (sum(list(range(0,number + 1))))**2
    return n

def sum_of_squares(number):
    ''' Param: int - number given by user
        Return: int - square of sum of numbers in number given'''
    a = []
    n1 = list(range(0,(number+1)))
    for x in n1:
        a.append(x**2)
    return sum(a)

def sum_of_squares1(number):
    return sum(a**2 for a in range(0,number+1))#More efficient way

def difference_of_squares(number):
    '''Param: int -  number given by user
       Return: int - substraction of numbers returned by the two functions'''
    return (square_of_sum(number) - sum_of_squares(number))

if __name__=='__main__':
    number = int(input('Favor ingresar numero\n'))
    print(square_of_sum(number))
    print(sum_of_squares(number))
    print(sum_of_squares1(number))
    print(difference_of_squares(number))
