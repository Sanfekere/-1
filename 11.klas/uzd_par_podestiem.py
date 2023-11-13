import math

def materialuAprekins(garums, platums, augstums, skaits):
    garums = math.round(garums, 1)
    platums = math.round(platums, 1)
    augstums = math.round(augstums, 1)
    skaits = math.round(skaits, 0)


def materialUzskaite(tips, izmers1, izmers2, skaits):

    tips = {'FINIERIS': izmers1*izmers2, 'LISTE': izmers1, 'STURIS': None}

while True:
    print('Ievadiet start lai sāktu programmu(beigt lai izietu)')
    ievade = input().strip().lower()

    print("Jūs ievadijāt : ", ievade)
    if ievade == 'start':
        cena = float(input("Ievadiet linoleja cenu par m2: "))
        lplatums = float(input("Ievadiet linoleja platumu: "))
        tplatums = float(input("Ievadiet telpas platumu: "))
        tgarums = float(input("Ievadiet telpas garumu: "))
        print(gridas_izmaksa(cena, lplatums, tplatums, tgarums))
    elif ievade == 'beigt':
        break


print('Programma beidza darbu!')

