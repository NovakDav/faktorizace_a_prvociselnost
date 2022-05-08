
#Funkce Sundaram_Sieve, pro otestování prvočíselnosti parametru number pomocí Sundaramova síta
def Sundaram_Sieve(number):
    if number > 1:
        if number ==2:
            return True

        if number == 3:
            return True


        # vytvoření pole num_list o velikostu number, a naplnění jej čísly od 1 do number
        num_list = [i + 1 for i in range(number)]

        #for cyklus iterující i, pro vzorec i+j+2*i*j, kde následně přiřadíme j = i tak aby sme zaručili, že j nebode menší než i,
        #while cyklus nám zvyšuje j do doby, než vzorec vypočte hodnotu větší enž je number, pokud vzorec vypočte hodnotu
        #která se nachází v num_list odstraní ji z tama
        for i in range(1, number // 2 + 1):

            j = i;
            while (i + j + 2 * i * j) <= number:

                if (i + j + 2 * i * j) in num_list:
                    num_list.remove(i + j + 2 * i * j)
                j += 1;

        prime = []

        #for cyklus, který nám vezme všechny členy z num_list*2 +1 a přidá je do pole prime
        for i in range(0, len(num_list)):
            prime.append(num_list[i] * 2 + 1)

        if number in prime:

            return True

        else:
            return  False

    else:
        return False
