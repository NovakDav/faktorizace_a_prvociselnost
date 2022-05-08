import math
#funkce Factorization, která vrací dělitele parametru n
def Factorization(n):
    factors = []

    #for cyklus procházející čísla od 2 po odmocninu čísla n zaokrouhlenou nahoru
    #pokud je n dělitené číslem rovno i, uloží i do pole factors
    for i in range(2,math.ceil(math.sqrt(n))):
        if n % i == 0:

            factors.append(i)
        while n % i == 0:
            n= n // i

    #pokud nenajdeme i, které dělí n, do pole factors přidáme samotné n
    if n>2:
        factors.append(n)
    return factors