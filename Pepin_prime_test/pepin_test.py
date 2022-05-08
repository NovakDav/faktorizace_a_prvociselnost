#funkce pro rozpoznání zda zvolené číslo n, je Fermatovo číslo
def Is_fermat(n):
    fermat_number = 0
    k=0
    #while cyklus, který počítá Fermatova čísla do té doby dokud nejsou menší nebo rovna
    # číslu n
    while fermat_number <= n:
        #výpočet fermatova čísla pomocí vzorce 2^2^k  +1
        fermat_number = pow(2, pow(2, k)) + 1
        if fermat_number == n:
            return True
        k+=1

    return False

#funkce pro testování zda fermatovo číslo,předané v parametru jako n, je prvočíslem
def Pepin_pt(n):
    if Is_fermat(n):
        #elitní prvočísla, která se nejčasněti dosazují za p ve vzorci pro otestování prvočíselnosti
        elite_primes=[3, 5, 7, 41, 15361, 23041, 26881, 61441, 87041,
                  163841, 544001, 604801, 6684673, 14172161]


        #for cyklus procházející elitní prvočísla
        for i in range (0,len(elite_primes)):
            #podmínka zda platí vzorec pro dané prvočíslo
            if pow(elite_primes[i],(n-1)//2,n) == (-1 % n):
                return True

    else:
        return False

