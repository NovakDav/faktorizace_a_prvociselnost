import math
#funkce is_quadratic pro zjištění zda parametr n je v kvadratickém tvaru
def is_quadratic(n):
    if n == 0  :
        return 0
    #pokud odmocnina z n je beze zbytku dělitelná číslem 1 víme, že je odmocnina celé číslo
    #tedy n je v kvadratickém tvaru
    if math.sqrt(n) % 1 ==0:
        return 1

    else:
        return -1


#funkce Quadratic_sieve_method pro faktorizaci parametru n pomocí kvadratického síta
def Quadratic_sieve_method(n):
    #pokud je n dělitelné 2 beze zbytku vrátíme faktory jako 2 a n/2
    if n % 2 == 0:
        return[2,n/2]

    #pokud samotné n je v kvadratickém tvaru vrátíme faktory jako odmocniny z n
    if(is_quadratic(n)):
        return [math.sqrt(n),math.sqrt(n)]

    #spodní limit od kterého budeme hledat prvek y^2 v rovnici x^2 ≡ y^2 (mod n)
    bottom_limit = math.ceil(math.sqrt(n))

    #for cyklus pro hledání y v rozmezí bottom limit<y<=n-1
    for i in range(bottom_limit+1,n-1):

        #testujeme zda výsledek x^2 mod n je v kvadratickém stavu pokud ano našli jsme faktory
        maybe_factor = pow(i,2) % n
        if is_quadratic(maybe_factor)==1:

            first_factor = i-math.sqrt(maybe_factor)
            second_factor = i+math.sqrt(maybe_factor)

            return [first_factor,second_factor]


    return False
