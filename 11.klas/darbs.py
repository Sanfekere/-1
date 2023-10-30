def pasuti_tkreklus(skaits, apdruka, piegade):

    cena_apdruka = {'TEKSTS': 5, 'ZIME': 7, 'FOTO': 20}

    apdrukas_cena = cena_apdruka.get(apdruka, 0) * skaits

    summa_pirms_atlaides_un_piegades = apdrukas_cena

    if summa_pirms_atlaides_un_piegades > 100:
        summa_pirms_atlaides_un_piegades *= 0.95

    if piegade and summa_pirms_atlaides_un_piegades < 50:
        piegades_maksa = 15
    else:
        piegades_maksa = 0

    kopsumma = summa_pirms_atlaides_un_piegades + piegades_maksa

    return kopsumma

cena = pasuti_tkreklus(50, 'ZIME', True)
print(cena)