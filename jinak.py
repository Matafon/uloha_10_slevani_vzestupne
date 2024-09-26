def sloucit_a_seřadit(seznam_1, seznam_2):
    slouceny_seznam = seznam_1 + seznam_2
    serazeny_seznam = []
    
    while slouceny_seznam:
        min_hodnota = slouceny_seznam[0]
        for i in slouceny_seznam:
            if i < min_hodnota:
                min_hodnota = i
        serazeny_seznam.append(min_hodnota)
        slouceny_seznam.remove(min_hodnota)
    
    return serazeny_seznam

seznam_1 = [int(x) for x in input("Zadej hodnoty seznamu:" ).split(',')]
seznam_2 = [int(x) for x in input("Zadej hodnoty seznamu:" ).split(',')]

print(sloucit_a_seřadit(seznam_1, seznam_2))