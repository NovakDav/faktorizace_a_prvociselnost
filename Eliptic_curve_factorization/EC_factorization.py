#funkce gcd pro hledání největšího společného dělitele parametrů a,b
def gcd(a,b):
    if a ==b:
        return a

    while b != 0:
        a, b = b, a % b
    return a

#funkce eliptic pro faktorizaci parametru n, parametry max_a, max_x, max_y udávají největší hodnoty v křivce 𝑦^2≡𝑥^3+𝑎𝑥+𝑏
def eliptic(n,max_a,max_x,max_y):

    if(n % 2) == 0:
        return [2, n/2]
    if(n % 3) == 0:
        return [3, n/3]

    #for cykly iterující hodnoty i, j, k do max hodnot určených parametry max_a, max_x, max_y, kdy i = max_a, j=max_x a k=max_y
    for i in range(0, max_a):
        for j in range(0, max_x):
            for k in range(0, max_y):

                a = i
                point = [j, k]

                #výpočet b z rovnice 𝑦^2≡𝑥^3+𝑎𝑥+𝑏 pomocí hodnoty a  a bodu na křivce se souřadnicemi [max_x,max_y]
                b = (pow(point[1], 2) - a * point[0] - pow(point[0], 3)) % n

                #výpočet křivky pomocí 4a^3 +27b^2
                curve = 4 * pow(a, 3) + 27 * pow(b, 2)


                #pokud NSD křivky a n je různé od 1 a zároveň různé od n, našli jsme faktory čísla n
                if gcd(curve, n) != 1 and gcd(curve, n) != n:
                    return [gcd(curve, n), n / gcd(curve, n)]

    return f"After reaching all bounds we found no factor!"


