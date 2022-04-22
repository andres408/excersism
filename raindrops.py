'''This program converts a number into a string that contains raindrop sound'''
def convert(number=0):
    a='Pling'
    b='Plang'
    c='Plong'
    d = number%3
    e = number%5
    f = number%7
    if d==0 and e==0 and f==0:
        return a+b+c
    if e==0 and f==0:
        return b+c
    if d==0 and e==0:
        return a + b
    if d==0 and f==0:
        return a + c
    if d==0:
        return a
    if e==0:
        return b
    if f==0:
        return c
    return str(number)


if __name__=='__main__':
    print(convert(number=8))
