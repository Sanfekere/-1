import math

def gridas_izmaksa(cena, lplatums, tplatums, tgarums):
    lmetra_kvads = cena
    lplatums = math.ceil(lplatums)
    tplatums = math.ceil(tplatums)
    tgarums = math.ceil(tgarums)

    neplinolejs = tplatums * tgarums

    izmaksas = lmetra_kvads * neplinolejs
    return izmaksas


while True:
    print('Ievadiet start lai sāktu programmu(beigt lai izietu)')
    ievade = input().strip().lower()

    print("Jūs ievadijāt : ", ievade)
    if ievade == 'start':
        cena = float(input("Ievadiet linoleja cenu par m3: "))
        lplatums = float(input("Ievadiet linoleja platumu: "))
        tplatums = float(input("Ievadiet telpas platumu: "))
        tgarums = float(input("Ievadiet telpas garumu: "))
        print(gridas_izmaksa(cena, lplatums, tplatums, tgarums))
    elif ievade == 'beigt':
        break


print('Programma beidza darbu!')