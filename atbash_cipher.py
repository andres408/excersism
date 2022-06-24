voc=[ chr(i) for i in range(97,123)]
v = voc[::-1]
def encode(plain_text):
    encoded_text=''
    for c in plain_text.lower():
        if c not in v:
            encoded_text += c
        if c in v:
            encoded_text += voc[v.index(c)]   
    return encoded_text
def decode(ciphered_text):
    decoded_text=''
    for chr in ciphered_text.lower():
        if chr not in v:
            decoded_text += chr
        if chr in v:
            decoded_text += v[voc.index(chr)]
    return decoded_text
