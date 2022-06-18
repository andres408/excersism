import string
a = (string.ascii_lowercase*2)
u = (string.ascii_uppercase*5)
b = []
def rot(text,key):
    for i in text:
        if i not in string.ascii_letters:
            b.append(i)
        if i in a:
            b.append(a[a.index(i) + key])
        if i in u:
            b.append(u[u.index(i) + key])
    return ''.join(b)
    
if __name__=='__main__':
    text=str(input('Ingrese text\n'))
    key = int(input('Ingrese key\n'))
    print(rot(text,key))
