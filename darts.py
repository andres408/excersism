'''Program to calculate points in dart game'''
def score(x, y):
    '''Param: float - coordinates of concentric circle
        return : int - points according concentric circle'''
    r =  (x**2 + y**2)**0.5
    if r <= 1:
        return 10
    if r <= 5 and r > 1:
        return 5
    if r <=10 and r > 5:
        return 1
    else:
        return 0

if __name__=='__main__':
    x = int(input('Ingrese una coordenada para x\n'))
    y = int(input('Ingrese una coordenada para y\n'))
    print(score(x,y))
