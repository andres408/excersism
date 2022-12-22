'''Program to check if a text is a Pangram'''
import string
def is_pangram(sentence):
    '''Param: str - sentence introduced by user
       return: bool - True if it pangram False otherwise'''
    a = list(string.ascii_lowercase)
    for i in sentence.lower():
        if i in a:
            a.pop(a.index(i))
    return not a

if __name__=='__main__':
    sentence = str(input('Ingresa una palabra '))
    print(valid(sentence))
