'''Program to return the values of the color bands and all the color bands of the resistors'''

def color_code(color):
    color_bands = ['black','brown','red','orange','yellow',
               'green','blue','violet','grey','white']
    '''Param: str - Color band introduced by user
       Return: int - Numerical value associated with the color band introduced'''
    colors =[]
    color_list = [x.strip() for x in color.split(' ')]
    for i in color_list:
       colors.append(color_bands.index(i))

    return ''.join(str(x) for x in colors[:2])
   
if __name__=='__main__':
    color = str(input('Enter a color band\n'))
    print(color_code(color))

