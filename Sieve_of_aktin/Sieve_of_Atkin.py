import math

# Základní funkce Atkinova síta, kde parametr number značí číslo, které chceme otestovat

def Sieve_of_atkin(number):

    if number == 2:
        return True

    elif number == 3:
        return True

    prime = [i + 1 for i in range(number)]
    top_limit = round(math.sqrt(number))

    #Upravené Erasthotenesovo síto s jehož pomocí si odebereme všechna složená čísla menší nebo rovna
    #než number z pole prime
    for i in range(2, top_limit+1):
        for j in range(2, (number//i)+1):
            rem_num = i*j
            if rem_num in prime:
                prime.remove(rem_num)


    numMod = number %60
    

    if numMod in prime:

        #Cykly pro hledání takového x a y, které budou splňovat rovnice k daným zbytkům dělení
        #pokud takové x a y nalezneme testované číslo je prvočíslem.
        x = 1
        while x * x <= number:
            y = 1
            while y * y <= number:

                # pokud numMod%4 = 1 tak provedeme zkoušku zda existuje taková rovnice kde platí
                # 4x^2 +y^2 = number, pokud ano číslo je prvočíslem

                if numMod % 4 == 1 and number == (4 * math.pow(x, 2)) + (math.pow(y, 2)):
                    return True

                # pokud numMod%6 = 1 tak provedeme zkoušku zda existuje taková rovnice kde platí
                # 3x^2 +y^2 = number, pokud ano číslo je prvočíslem

                elif numMod % 6 ==1 and number == (3 * math.pow(x,2)) + (math.pow(y,2)):
                     return True

                # pokud numMod%12 = 1 tak provedeme zkoušku zda existuje taková rovnice kde platí
                # 3x^2 -y^2 = number, pokud ano číslo je prvočíslem

                elif numMod %12 == 1 and number ==(3 * math.pow(x, 2)) - (math.pow(y, 2)):
                     return True

                y += 1
            x += 1
    else:
        return False






