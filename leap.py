'''Program to determine if a year is leap or not'''
def leap(year):
    ''' Param: int - a given year
        Return: Bool - True if leap year, False if not'''
    a =  year%4
    b = year%100
    c = year%400
    if a == 0 and b == 0 and c == 0:
        return True
    if a == 0 and b == 0:
        return False
    if a == 0:
        return True
    return False
if __name__=='__main__':
    year= int(input('ingresa un año\n'))
    print(leap(year))
