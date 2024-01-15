vardnica = {
    'suns' : {'en' : 'dogs', 'de' : 'Hund'},
    'kakis' : {'en' : 'cat', 'de' : 'Katze'}
}

while True:
    print('Ievadiet tulkojamo vārdu latviešu valodu(beigt lai izietu)')
    ievade = input().strip().lower()

    print("Jūs ievadijāt : ", ievade)

    if ievade == 'beigt':
        break

    print('Programma vēl darbojas!!!')

print('Programma beidza darbu!')