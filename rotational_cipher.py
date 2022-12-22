import string
a = (string.ascii_lowercase*2)
u = (string.ascii_uppercase*5)
d = ('1234567890'*5)
p = ('<>,.-_:;/&%$#\"\'?¿=*+-!' * 5)
b = []
def rot(text,key):
    for i in text:
        if i in p:
            b.append(p[p.index(i) + key])
            b.append(p[p.index(i) + 2 + key])
        if i in string.digits:
            b.append(d[d.index(i) + key])
            b.append(d[d.index(i) + 2 + key])
        if i in a:
            b.append(a[a.index(i) + key])
            b.append(a[a.index(i) + 2 + key])
        if i in u:
            b.append(u[u.index(i) + key])
            b.append(u[u.index(i) + 2 + key])
    return ''.join(b)
    
if __name__=='__main__':
    text=str(input('Ingrese text\n'))
    key = int(input('Ingrese key\n'))
    print(rot(text,key))
