'''Solution to grains exercise'''
def square(number):
    '''
    param:int corresponding a number in the chessboard
    Return the number of grains in the number of the position in the chess board.
    '''
    if number < 1 or number >64:
        raise ValueError('square must be between 1 and 64')
    return  2**(number-1)

def total():
    '''
    param: It is fixed to the total number of places in chessboard
    Return: The total number of grains in the chessboard
    '''
    return 2 ** 64-1

if __name__=='__main__':
    print(square(number=20))
    print(total())
        
        
