a = "H'-1WD9U?lrk/2u{=3Icnzp*&)ZbRj}iF>8em[]70BfA4\"OC5%!N,_Qqh6g;.$VTG(YysMKX:<@EoJPw#Latx+vdS\|\\\\\\\\H'-1WD9U?lrk/2u{=3Icnzp*&)ZbRj}iF>8em[]70BfA4\"OC5%!N,_Qqh6g;.$VTG(YysMKX:<@EoJPw#Latx+vdS\|\\\\\\\\H'-1WD9U?lrk/2u{=3Icnzp*&)ZbRj}iF>8em[]70BfA4\"OC5%!N,_Qqh6g;.$VTG(YysMKX:<@EoJPw#Latx+vdS\|\\\\\\\\H'-1WD9U?lrk/2u{=3Icnzp*&)ZbRj}iF>8em[]70BfA4\"OC5%!N,_Qqh6g;.$VTG(YysMKX:<@EoJPw#Latx+vdS\|\\\\\\\\H'-1WD9U?lrk/2u{=3Icnzp*&)ZbRj}iF>8em[]70BfA4\"OC5%!N,_Qqh6g;.$VTG(YysMKX:<@EoJPw#Latx+vdS\|\\\\\\\\H'-1WD9U?lrk/2u{=3Icnzp*&)ZbRj}iF>8em[]70BfA4\"OC5%!N,_Qqh6g;.$VTG(YysMKX:<@EoJPw#Latx+vdS\|\\\\\\\\H'-1WD9U?lrk/2u{=3Icnzp*&)ZbRj}iF>8em[]70BfA4\"OC5%!N,_Qqh6g;.$VTG(YysMKX:<@EoJPw#Latx+vdS\|\\\\\\\\H'-1WD9U?lrk/2u{=3Icnzp*&)ZbRj}iF>8em[]70BfA4\"OC5%!N,_Qqh6g;.$VTG(YysMKX:<@EoJPw#Latx+vdS\|"
b = []
def codificar(text,key):
    for i in text:
        if i in a:
            b.append(a[a.index(i) + key])
            b.append(a[a.index(i) + 2 + key])       
    return ''.join(b)

def descodificar(text, key):
    for i in range(0,len(text),2):
        if text[i] in a:
            if descodificar:
                b.append(a[a.index(text[i]) - key])
    return ''.join(b)

if __name__=='__main__':
    funcion=input('Ingrese la funcion requerida codificar o descodificar\n (c,d)')
    text=input('Ingrese text\n')
    key = int(input('Ingrese key\n'))
    if funcion == 'c':
        print(codificar(text,key))
    elif funcion == 'd':
        print(descodificar(text,key))
    else:print('Ingrese una opcion valida')
