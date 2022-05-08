#funkce gcd nám zjišťuje největšího společného dělitele parametrů a a b
def gcd(a,b):
    if a ==b:
        return a

    while b!=0:
        a, b = b, a % b
    return a

#funkce pro Pollardovu rho faktorizaci , n je parametr čísla, které chceme faktorizovat
def Rho_factorization(n):
    if n == 1:
        return n

    if n % 2 == 0:
        return [2,n/2]

    x = [0] * n
    x[0]=2

    #for cyklus pro výpočet x_i-x_(i-1)
    x[0] = 2
    for i in range(1, n):
        x[i] = pow(x[i-1],2)+1
        #podmínka pro zjištění zda NSD(x_i-x_(i-1),n) != 1, pokud ano našli jsme faktor čísla n
        if gcd(x[i]-x[i-1], n) != 1:

            first_factor = gcd(x[i]-x[i-1],n)
            second_factor = n / first_factor

            return [first_factor, second_factor]

    return n
