'''Program to return stablished responses'''
import time

#start = time.time()
def response(hey_bob):
    '''Param: str - introduced by user
       Return: str -  Stablishe responses
    '''
    hey_bob = hey_bob.strip()
    if not hey_bob or len(hey_bob) == 0:
        return 'Fine. Be that way!'
    if hey_bob.isupper() == True and hey_bob[-1] == '?':
        return 'Calm down, I know what I\'m doing!'
    if hey_bob[-1] == '?':
        return 'Sure.'
    if hey_bob.isupper():
        return 'Whoa, chill out!'
    return 'Whatever.'

if __name__=='__main__':
    hey_bob = str(input('Ingresa tus palabras\n'))
    start = time.time()
    print(response(hey_bob))

end = time.time()

print(end - start)
