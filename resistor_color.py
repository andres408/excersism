'''Program to return the values of the color bands and all the color bands of the resistors'''
def color_code(color):
    '''Param: str - Color band introduced by user
       Return: int - Numerical value associated with the color band introduced'''
    return colors().index(color)


def colors():
    '''Return : list - different color bands'''
    color_bands = ['Black','brown','red','orange','yellow',
    'green','blue','violet','grey','white']
    return color_bands

if __name__=='__main__':
    color = str(input('Enter a color band\n'))
    print(color_code(color))
