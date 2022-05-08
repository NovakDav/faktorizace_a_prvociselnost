import math

#funkce gcd nám zjišťuje největšího společného dělitele parametrů a a b
def gcd(a,b):

    if a ==b:
        return a

    while b!=0:
        a, b = b, a % b
    return a

#funkce Euler_method(n) pro nalezení faktorů čísla n, dle Eulerovy faktorizační metody
def Euler_method(n):

    if n % 2 == 0:
        return [2,n/2]
    a=-1
    b=-1
    c=-1
    d=-1

    #for cyklus hledající čísla a a b, a je rovno odmocnině z n - i^2, pokud je a kvadratickým zbytkem
    # potom b = i
    for i in range(0,n):
        if i*i <=n:
            a = math.sqrt(n-(i*i))
            if(a % 1==0):
                b=i
                break

    # for cyklus hledající čísla c a d, a je rovno odmocnině z n - j^2, pokud je b kvadratickým zbytkem
    # potom d = j, zároveň oba prvky musí být různé od a,b
    for j in range(0, n):
        if b!= j and j*j <=n:
            c= math.sqrt(n-(j*j))
            if(c % 1 == 0):
                d=j
                break

    #pokud jsme nenašli a,b,c,d vrátíme false
    if( a == -1 or b == -1 or c == -1 or d==-1):
        return False


    k=gcd(a-c,d-b)
    l = (a-c)/k
    m = (d-b)/k
    h = (a+c)/m


    #pokud je k dělitelné 2 , prvního dělitele vydělíme 4
    if(k%2==0):
        first_factor = (pow(k, 2) + pow(h, 2))/4
        second_facttor = (pow(m, 2) + pow(l, 2))
    #ve zbylých případech oba delitele vydělíme 2
    else:
        first_factor = (pow(k,2)+pow(h,2))/2
        second_facttor = (pow(m,2)+pow(l,2))/2

    return[first_factor,second_facttor]