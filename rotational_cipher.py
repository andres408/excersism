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
        if i in string.digits:
            b.append(d[d.index(i) + key])
        if i in a:
            b.append(a[a.index(i) + key])
        if i in u:
            b.append(u[u.index(i) + key])
    return ''.join(b*2)
    
if __name__=='__main__':
    text=str(input('Ingrese text\n'))
    key = int(input('Ingrese key\n'))
    print(rot(text,key))
