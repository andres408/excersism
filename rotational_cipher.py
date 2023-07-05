import string
a = (string.printable*2)
b = []
def rot(text,key):
    for i in text:
        if i in a:
            b.append(a[a.index(i) + key])
            b.append(a[a.index(i) + 2 + key])
        
    return ''.join(b)


if __name__=='__main__':
    text=str(input('Ingrese text\n'))
    key = int(input('Ingrese key\n'))
    print(rot(text,key))
