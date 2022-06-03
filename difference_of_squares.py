def square_of_sum(number):
    n = (sum(list(range(0,number + 1))))**2
    return n

def sum_of_squares(number):
   ''' a = []
    n1 = list(range(0,(number+1)))
    for x in n1:
        a.append(x**2)
    return sum(a)'''
   return sum(a**2 for a in range(0,number+1))#Hace lo mismo que las lineas de arriba pero mas eficiente.

def difference_of_squares(number):
    return (square_of_sum(number) - sum_of_squares(number))

if __name__=='__main__':
    number = int(input('Favor ingresar numero\n'))
    print(square_of_sum(number))
    print(sum_of_squares(number))
    print(difference_of_squares(number))
