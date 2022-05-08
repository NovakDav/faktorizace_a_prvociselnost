#Fermatův test prvočíselnosti , parametr n je testované číslo
def Fermat_pt(n):

    if n == 2:
        return True

    if n % 2 == 0:
        return False
    # pomocí for cyklu projíždíme všechna a ve vzorci a^n-1 ≡ 1 (mod n), pokud takové číslo nalezneme víme,
    #že číslo n je složené
    for a in range(2, n-1):
        if pow(a, n - 1) % n != 1:
            return False
    return True