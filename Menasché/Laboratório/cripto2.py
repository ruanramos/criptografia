from math import *

def divisao(a,b):
    q=0
    r=a
    x=[]
    if r<b:
        list.append (x, q)
        list.append (x,r)
        return x
    while r>=b:
            r-=b
            q+=1
            if r<b:
                list.append (x, q)
                list.append (x,r)
                return x

def euclidiano(a,b):
    r = a%b
    while r!=0:
        a = b
        b = r
        r = a%b
    return b

def euclidianoEstendido(a,b): #retorna uma lista do tipo [mdc, alpha, beta]
    r = a
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    while r != 0: 
        r = a%b
        q = a//b
        x = x0 - x1*q
        y = y0 - y1*q
        x0 = x1
        x1 = x
        y0 = y1
        y1 = y
        a = b
        b = r
    d = a
    alpha = x0
    beta = y0
    return [d, alpha, beta]
    
    
def eqDiofantina(a,b,c): #chama a funcao do euclidiano estendido
    lista = euclidianoEstendido(a,b)
    if c%lista[0] != 0: #checa se existe x e y inteiro tal que alpha.x + beta.y = c1 * d
        return [0, 0]
    else:
        c1 = c//lista[0]
        return [c1*lista[1], c1*lista[2]] #x = alpha*c1 e y = beta*c1

def fatIngenuo(n): #retorna o menor fator primo de n
    f = 2
    while f <= int(sqrt(n)):
        if n%f == 0:
            return f
        else:
            f += 1
    return n


def fatIngenuoCompleto(n): #retorna a fatoracao completa de n, uma lista
    f = 2                  #com os expoentes outra com os fatores
    fatores = []
    expoentes = []
    while f <= int(sqrt(n)):
        cont = 0
        if n%f == 0:
            while n%f == 0:
                n = n/f
                cont += 1
            fatores.append(f)
            expoentes.append(cont)
        else:
            f += 1
    fatores.append(n)
    expoentes.append(1)
    return [fatores, expoentes]
    
    
def fatFermat(n): #retorna dois fatores de n 
    if n % 2 == 0:
        while n % 2 == 0:
            n = n/2
    x = int(sqrt(n))
    y = 0
    while n != (x*x - y*y):
        x += 1
        y = int(sqrt(x*x - n))
        if x == (n+1)/2:
            return [1, n]
    return [(x-y), (x+y)]

def sieve(n):
  primes = [2]
  numbers = [n for n in range(n+1)] # i == numbers[i]

  for i in range(3, n+1 , 2): # i de 3 até o último da lista, passando só pelos ímpares
    if numbers[i] == 0: # "risquei" esse número, então ele não é primo.
      continue

    # Se chegou aqui, não risquei o número, então ele é primo.
    primes.append(i)

    for j in range(i * i, n+1, i): # começando em i^2 até o limite da lista, de i em i
      numbers[j] = 0 # risca o número

  return primes # retorna a lista de primos.
