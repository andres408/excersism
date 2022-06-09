'''Program to change words according to pig latin game rules.'''
vowels=['a','e','i','o','u']
vowelsa=['xr','yt']

def words(word):
    '''Param: str - word from translate function
       Return : str - word with suffix according to game rules'''
    b = 0
    vowelsound= word[0] in vowels or word[:2] in vowelsa
    cluster= word[:2] not in vowels and word[:2] not in vowelsa
    if vowelsound:
        return word + 'ay'
    if not vowelsound and word[1:3] == 'qu':
        return word.strip(word[:3]) + word[:3] + 'ay'
    if len(word) == 2 and word[1] == 'y':
        return word.strip(word[0]) + word[0] + 'ay'
    if cluster and word[2] == 'y':
        return word.strip(word[:2]) + word[:2] + 'ay'
    if word[:2] =='qu':
        return word.strip(word[:2]) + word[:2] +'ay'
    if not vowelsound:
        for a in word[:3]:
            if a not in vowels:
                b += 1
            if b == 3:
                return word[3:] + word[:3] +'ay'
        if word[1] not in vowels:
            return word.strip(word[:2]) + word[:2] + 'ay'
        return word.strip(word[0]) + word[0] + 'ay'

def translate(text):
    '''Param: str -  word or words introduced by user
        Return: str - the changed words in order according to words function.'''
    return ' '.join(words(word) for word in text.split())

if __name__=='__main__':
    text = str(input('Ingresa palabra\n'))
    print(translate(text))
