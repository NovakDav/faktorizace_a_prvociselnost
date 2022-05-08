#funkce pro výpočet jednotlivého členu polynomu
def member_of_poly(n,i):

    if i == 0:
        return 1
    #for cyklus pro výpočet faktoriálu čísla i
    factorial = i
    for j in range(i-1,0,-1):
        factorial = factorial * j

    #for cyklus pro výpočet n(n-1)(n-2)... na základě i
    number = n;
    for k in range(0,i-1):
        n-=1
        number *=(n)

    number = number / factorial
    return number

def AKS_test(n):
    polynom= [0] * (n+1)

    if n>1 and n <3:
        return True

    if n>2:
        #for cyklus který pomocí funkce member_of_poly počítá jednotlivé prvky a ukládá je do pole polynom
        for i in range(0,n+1):
            polynom[i]=member_of_poly(n,i)


        #for cyklus na průchod polem polynom a testování jejich dělitelnosti číslem n
        for member in range(1,n):
            if polynom[member]%n !=0:

                return False

        return True
    else:
        return False