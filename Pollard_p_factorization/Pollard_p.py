#funkce pro výpočet faktoriálu,čísla předaného
def factorial(fac):
    result =fac
    for j in range(fac - 1, 0, -1):
        result = result * j
    return result

#funkce gcd nám zjišťuje největšího společného dělitele parametrů a a b
def gcd(a,b):
    if a ==b:
        return a

    while b!=0:
        a, b = b, a % b
    return a

#funkce pro Pollardovu p-1 faktorizační metodu, parametr n je číslo u kterého provádíme faktorizaci
def Factorization_method(n):
    a =2
    left_side =0
    found_factor = False

    #dva vnořené cykly které nám hledají a, k ve vzoci (a^k!)-1, a nám začíná od 2
    #pokud najdeme takové a,k kde NSD ((a^k!)-1,n) != 1 while cykly skončí a uložíme si do proměnné
    #left_side hodnotu (a^k!)-1
    while found_factor==False:
        k=1
        while found_factor== False:
            left_side = pow(a,factorial(k))-1
            if gcd(left_side,n)!=1:
                found_factor = True
            else:
                k+=1
        a+=1

    if gcd(left_side,n) != n:
        return [gcd(left_side,n),n/gcd(left_side,n)]
    else:
        return False

