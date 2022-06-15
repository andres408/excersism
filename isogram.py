import string
def compare(text):
    a = [i for i in text.lower() if i in string.ascii_lowercase]
    b=[]
    for x in sorted(a):
        if x not in b:
            b.append(x)
            a.pop(a.index(x))
    
    return not a

if __name__=='__main__':
    text=str(input('Ingresa un texto\n'))
    print(compare(text))
