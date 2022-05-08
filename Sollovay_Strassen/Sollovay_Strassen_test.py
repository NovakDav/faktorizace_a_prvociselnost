import math
#funkce pro zjištění zda je parametr n ve kvadratickém tvaru
def is_quadratic(n):
    if n == 0  :
        return 0
    #pokud odmocnina rozdíl odmocniny n a zaokrouhlené odmocniny z n je roven 0 číslo
    #n je ve kvadratickém tvaru
    if math.sqrt(n)- math.floor(math.sqrt(n)) ==0:
        return 1

    else:
        return -1

#funkce pro výpočet jacobiho symbolu pro čitatel i a jmenovatel n )i/n)
def jacobi(i, n):
    jacobi = 1

    #dokud i je různé od 0
    while (i != 0):

        #while cyklus pro zbavení se sudých dělitelů čísla i
        while (i % 2 == 0):
             i = i/2

             #kontrola pravidla zda je zbytek po dělení čísla n číslem 8
             #roven 3 nebo 5
             if (n % 8 ==3) or ( n % 8 == 5):
                 jacobi = -jacobi
        i,n = n,i
        #kontrola pravidla zda jsou oba členy liché
        if(i % 4 == 3) and (n % 4 ==3 ):
            jacobi=-jacobi
        i= i % n

    return jacobi

#Základní funkce pro Sollovay-Strassenův algoritmus testování prvočíselnosti
#kde parametr n je testované číslo
def Primality_test(n):

    prime_count=0
    composite_number=0

    #for cyklus pro testování všech čísel v rozmezí 2 až n
    for i in range(2,n):

        #levá strana rovnice zkoumá zda a je kvadratický zbytek pro i^((n-1)/2) ≡ 1 (mod n)
        left = is_quadratic(pow(i,(n-1)//2,n))

        if jacobi(i,n)== 1 and left == 1:
            prime_count +=1
        elif jacobi(i,n)==-1 and left == -1:
            prime_count +=1

        else:
            composite_number+=1

    if(prime_count>=composite_number):
        return True
    else:
        return False