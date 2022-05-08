import math

#funkce Factorization_method(n) pro faktorizaci čísla n dle Fermazovy faktorizace
def Factorization_method(n):

    #pokud je n v kvadratickém stavu vrátíme jako faktory odmocninu
    square = math.floor(math.sqrt(n))
    if(square * square) == n:
        return[square,square]

    if(n <=1):
        return n
    if n % 2 == 0:
        return [2,n/2]

    #while cyklus pro hledání s ve vzorci n= sqrt(n+s^2)
    s=1
    while s<n:
        t = math.sqrt(n+math.pow(s,2))
        if t - math.floor(t) == 0:
            break
        s+=1

    #pokud t-s nebo t+s jsou rovny n, znamená to prvočíselnost n, vrátíme tedy [1,n]
    if t-s == n or t+s ==n:
        return [1,n]
    #v ostatních případech vrátíme faktory t-s a t+s
    else:
        return [t-s,t+s]