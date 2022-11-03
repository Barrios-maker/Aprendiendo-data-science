#La siguiente funcion representa cualquier funcion matematica
def funcion(x):
    return 100*(2.71**(-x/100))-(0.01*x**2)

def aproximar_raiz(a,b,e):
    '''
    aproximar_raiz(a,b,e) aproxima la raiz de una funcion matematica 
    llamada funcion(x) utilizando el metodo de la biseccion en 
    el intervalo [a,b] con un error menor a e 
    '''
    if funcion(a)*funcion(b)>0: # Este if sirve de advertencia, si no hay una raiz en [a,b] o si hay mas de una raiz  la funcion no funciona
        return('No hay una sola raiz en ese rango')
    i=0
    while ((b-a)/2)>e: # Comparacion entre error real y error minimo deseado 
        i=i+1
        m=(b+a)/2 # Punto medio
        y=funcion(m)
        if y*funcion(a)>0: #  Equivalente a decir if f(m) y f(a) tienen el  mismo signo
            a=m
        elif y*funcion(b)>0:
            b=m
    return (b+a)/2

print(aproximar_raiz(60,80,0.0001))
