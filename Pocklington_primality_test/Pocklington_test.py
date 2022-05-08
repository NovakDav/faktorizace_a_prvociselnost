import math

#funkce gcd nám zjišťuje největšího společného dělitele parametrů a a b
def gcd(a,b):
    while b!=0:
        a, b = b, a % b
    return a
#funkce pro Pocklingtonův test prvočíselnosti, parametr n je testované číslo
def Primality_test(n):
    if n ==1:
        return False
    if n == 2:
        return True

    # průchod všema p ve vzorečku p^(n-1) ≡ 1 (mod n)
    for p in range (2,n):
        #pokud jsme nalezli takové p, kde platí výše zmíněná rovnice pokračujeme k hledání q
        if pow(p,n-1)%n == 1:
            # for cyklus hledající q aby platila rovnice NSD(p^((n-1)/q),n)=1
            for q in range(math.ceil(math.sqrt(n))-1,n):
                #pokud jsme našli takové q číslo je prvočíslem
                if gcd(pow(p,(n-1)/q),n) == 1:
                    return True


        return False
    return False



