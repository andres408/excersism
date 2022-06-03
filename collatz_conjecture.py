'''Program to calculate steps of collatz conjecture'''
def steps(n):
    '''Param: Int - Positive number
       Return: Steps required to get 1'''
    if n > 0:
        s = 0
        while(n > 1):
            if n%2==0:
                n = n/2
            else:
                n = 3*n + 1
            s += 1
    else:
        raise ValueError('Only positive integers are allowed')
    return s

if __name__=='__main__':
    n=int(input('Introduce a number:\n'))
    print(steps(n))
