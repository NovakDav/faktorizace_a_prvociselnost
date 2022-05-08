#Funkce pro Miller*Rabinův test prvočíselnosti, kde parametr n je testované číslo
def Miller_Rebin_pt(n):

    prime_count=0
    composite_number = 0

    #For cyklus pro získání čísel s a d, pro která platí 2^s*d = n-1
    for s in range(0,n):
        for d in range (0,n+1):

            #podmínka pokud najdeme čísla s a d, kde uvedená rovnice platí ulžíme si hodnoty s,d
            if(n-1 == pow(2,s)*d):


                #for cyklus pro výpočet zda je číslo složené či prvočíslem pro všechna a v rovnici a^d ≡ 1 (mod n)
                #nebo a^((2^r)*d) ≡ -1 (mod n)
                for a in range(1,n):

                    #for cyklus pro dané a, který testuje všechny hodnoty r, splnující 0<=r<s
                    for r in range(0,s+1):

                        #pokud je r=0 rovnice pro testování prvočíselnosti je a^d ≡ 1 (mod n)
                        if r ==0:
                            if(pow(a,pow(2,r)*d)%n == 1):

                                prime_count+=1
                            else:
                                composite_number+=1

                        # pokud je r>0 rovnice pro testování prvočíselnosti je a^((2^r)*d) ≡ -1 (mod n)
                        if r>0:
                            if (pow(a,pow(2,r)*d)+1)%n==0:

                                prime_count += 1
                        else:

                            composite_number += 1

    #test zda nám vyšlo prvočíslo v minimálně 25% případů
    if(prime_count/(prime_count+composite_number))>= 1/4:
            return True

    else:
        return False


