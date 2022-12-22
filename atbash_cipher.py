'''Program to encode and decode a text'''
import string
voc=[ chr(i) for i in range(97,123)]
v = voc[::-1]
def encode(plain_text):
    '''Param: str - A plain text with numbers and symbols
       return: str - A encoded text changing the words for the word + 13 position in the alphabet, numbers stay equal. spaces and symbols are erasen and each 5 digits one space.'''
    encoded_text=''
    h = 0
    for c in plain_text.lower():
        if c.isspace() and c in string.punctuation:
            encoded_text += ''
        if c.isnumeric():
            encoded_text += c
            h +=1
        if c in v:
            encoded_text += voc[v.index(c)]
            h+=1
        if h==5:
            encoded_text +=' '
            h=0    
    return encoded_text.strip()
def decode(ciphered_text):
    '''Param: str - A encoded text
       return: str - A plain text without spaces'''
    decoded_text=''
    for chr in ciphered_text.lower():
        if chr.isspace() and chr in string.punctuation:
            decoded_text +=''
        if chr.isnumeric():
            decoded_text += chr
        if chr in v:
            decoded_text += v[voc.index(chr)]
    return decoded_text
    
if __name__=='__main__':
    plain_text=str(input('Ingresa palabra\n'))
    print(encode(plain_text))
    ciphered_text=str(input('Ingresa texto\n'))
    print(decode(ciphered_text))
