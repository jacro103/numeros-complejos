import libreria as lc

def suvectores(v,w) :
    n = len(v)
    print(n)
    r = [(0,0)] *n
    for k in range(n):
        r[k]=lc.cplxsum(v[k],w[k])
    return r

def invector(a):
    n = len(v)
    print(n)
    r = [(0,0)] * n
    for k in range(n):
        r[k] = lc.cplxmult((-1,0),v[k])
    return r
def multesc(c,v):
    n = len(v)
    print(n)
    r = [(0, 0)] * n
    for k in range(n):
        r[k] = lc.cplxmult(c, v[k])
    return r

def summa(a,b):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxsum(a[j][k],b[j][k])
    return r
def mulma(c,a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxmult(c,a[j][k])
    return r
def invma(a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0, 0)] * n
    r = [fila] * m
    for j in range(m):

        fila = [(0, 0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = lc.cplxmult((-1,0),a[j][k])
    return r

def trama(a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] = a[k][j]
    return r

def conma(a):
    m = len(a)
    n = len(a[0])
    print(m)
    print(n)
    fila = [(0,0)] * n
    r = [fila] * m
    for j in range (m):

        fila = [(0,0)] * n
        r[j] = fila
        for k in range(n):
            r[j][k] =  lc.cplxcon(a[j][k],0)

    return r
def addaga(a,b):

    return
def prodmat(a,b):
    n = len(a)
    print(n)
    r = [(0, 0)] * n

    for k in range(n):
        r[k]

    return r


if __name__ == '__main__':
    print("vectores")
    v = [(2,8),(8,9),(6,7)]
    w = [(7,0),(9,10),(2,3)]
    print(v)
    print(w)
    print("suma de vectores")
    print(suvectores(v,w))
    print(" inverso adictivo  de vectores")
    print(invector(v))
    print(" multiplicacion de escalar a vector")
    print(multesc((1,0),v))
    a = [[(2,3),(3,4),(3,2)],
         [(1,1),(1,1),(1,1)],
         [(2,2),(3,3),(4,4)]]
    b = [[(4,4),(3,6),(3,7)],
         [(1,2),(1,2),(1,2)],
         [(1,1),(2,2),(3,3)]]
    print("matrices")
    print(a)
    print(b)
    print("suma de matriz")
    print(summa(a,b))
    print(" inversa adictiva de una matriz")
    print(invma(a))
    print("multiplicacion escalar con matriz")
    print(mulma((1,0),a))
    print("traspuesta de una matriz")
    print(trama(a))
    print("conjuncion de matriz")
    print(conma(a))
    print("adjunta daga de matriz/ vector")
    s = [(1,0),(0,1),(0,2)]
    t = [(0,1),(0,1),(1,0)]
    print("Producto de dos matrices (de tamaños compatibles)")
    print(prodmat(s,t))
    print("Función para calcular una matriz sobre un vector.")
    print("Producto interno de dos vectores")
    print("norma de un vercor")
    print("Distancia entre dos vectores")
    print("Revisar si una matriz es unitaria")
    print("Revisar si una matriz es Hermitiana")
    print("Producto tensor de dos matrices/vectores")