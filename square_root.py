def square_root(number):
    """
    Given a positive integer number, return its square root.

    The function uses a while loop that will decrease the value of number by
    restando until number is less or equal than 0. The variable restando will
    increase by 2 in each iteration.

    Args:
        number (int): A positive integer

    Returns:
        int: The integer number of iterations needed to reach
             or pass the square root of number
    """
    restando = 1
    counter = 0
    original_number = number
    while number > 0:
        # Reduce number by restando
        number -= restando
        # Increase restando by 2 in each iteration
        restando += 2
        # Increase counter by 1 in each iteration
        counter += 1

    if counter ** 2 != original_number:
        print(f'El numero {original_number} no tiene una raiz cuadrada entera')
    else:    
        print(f'La raiz cuadrada de {original_number} es {counter}')




square_root(144)