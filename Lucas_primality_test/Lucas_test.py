from Trial_division import Trial_division

#funkce pro Lucasův test prvočíselnosti,parametr n je testované číslo
def Primality_test(n):
    #vytvoření pole pro dělitele n-1, dělitele získáme pomocí Trial_division
    factors = []
    factors = Trial_division.Factorization(n-1)

    #for cyklus pro iteraci p pro rovnici p^(n-1) ≡ 1 (mod n)
    for p in range (2,n):
        is_prime = True
        #pokud pro dané p rovnice p^(n-1) ≡ 1 (mod n) neplatí pokračujeme pro další p
        if(pow(p,n-1) % n !=1):
           continue

        #cyklus kontrolující zda p^((n-1)/q) ≢ 1 (mod n) pralí pro všechna q, pokud platí
        # pro všechna q, podmínka v cyklu nezmění proměnnou is_prime na False a podmínka za
        # cyklem vyhodnotí n jako prvočíslo
        for q in range(0,len(factors)):

            if pow(p,(n-1)//factors[q],n) ==1:
                is_prime = False

        if is_prime == True:
            return True

    return False



