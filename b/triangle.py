'''Solution to triangle exercise on exercism page.'''

def triangle(sides):
    ''' arg: three int with the length of each side of the triangle.
        return: Bool if it is a triangle or not.
    '''
    a,b,c = sides
    sides_more_than_zero = a > 0 and b > 0 and c > 0
    sum_sides_greater_than_other_side = a + b >= c and b + c >= a and c + a >= b
    return sides_more_than_zero and sum_sides_greater_than_other_side

    
def equilateral(sides):
    ''' arg: three int with the length of each side of the triangle.
        return: Bool if it is equilateral or not.
    '''
    a,b,c = sides
    return triangle(sides) and a == b and b == c

def isosceles(sides):
    ''' arg: three int with the length of each side of the triangle.
        return: Bool if it is isosceles or not.
    '''
    a,b,c = sides
    return triangle(sides) and(a== b or b == c or c == a)

def scalene(sides):
    ''' arg: three int with the length of each side of the triangle.
        return: Bool if it is a scalene or not.
    '''
    a,b,c = sides
    return triangle(sides) and (a != b and b != c)

if __name__=='__main__':
    print(equilateral(sides=[30,30,30]))
    print(isosceles(sides=[20,25,0]))
    print(scalene(sides =[1,3,3]))
