
def funcion(x):
    return 100*(2.71**(-x/100))-(0.01*x**2)

def aproximar_raiz(a,b,e):
    a=float(a)
    b=float(b)
    if funcion(a)*funcion(b)>0:
        return('No hay una sola raiz en ese rango')
    i=0
    while ((b-a)/2)>e:
        i=i+1
        m=(b+a)/2
        ##print(m)
        y=funcion(m)
        if y*funcion(a)>0:
            a=m
        elif y*funcion(b)>0:
            b=m
    return (b+a)/2

print(aproximar_raiz(60,80,0.0001))
