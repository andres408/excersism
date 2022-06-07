vowels=['a','e','i','o','u']
vowelsa=['xr','yt']

def words(word):
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
    if word[:3] not in vowels:
        return word.strip(word[:3]) + word[:3] + 'ay'
    if not vowelsound:
        if word[1] not in vowels:
            return word.strip(word[:2]) + word[:2] + 'ay'
        return word.strip(word[0]) + word[0] + 'ay'
        
if __name__=='__main__':
    word = str(input('Ingresa palabra\n'))
    print(words(word))
