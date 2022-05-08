#funkce Is_mersenne(n) nám počítá kolikátým Mersennovým číslem je zvolené číslo v parametru n
def Is_Mersenne(n):
    i=2

    count=1
    #while cyklus počítající Mersennova čísla a porovnává je s číslem n, pokud jsou stejná
    #vrátí se umístění čísla n mezí Mersennovými čísly
    while i < n:
        i=pow(2,count)-1

        if (i == n):

            return count
        count+=1
    return 0
#funkce pro Lucas-Lehmerův test prvočíselnosti Mersennových čísel
def Mersenne_num_primality_test(n):

    #podmínka určující zda zvolené číslo n je Mersennovým číslem, pokud ne vrátí se hodnota False.
    if Is_Mersenne(n)==0:
        return False

    else:
        s_1=4
        s_2=4
        #Výpočet 𝑆_n-2 pomocí vzorce s_n = (s_(n-1))^2 -2 kde s_1 = 4
        for i in range (1,Is_Mersenne(n)-1):
            s_1=s_2
            s_2=pow(s_1,2)-2

        #Pokud s_(n-2) % n jedná se o prvočíslo
        if s_2%n ==0:

            return True
        else:
            return False
