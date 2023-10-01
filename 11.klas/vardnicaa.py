# pip install deep-translator

from deep_translator import GoogleTranslator

vardnica = {
    'suns': {'en': 'dog', 'de': 'Hund'},
    'kaķis': {'en': 'cat'}
}

def tulkojums(ievaditais_vards, uz_valodu):
    if ievaditais_vards in vardnica:
        if uz_valodu in vardnica[ievaditais_vards]:
            return vardnica[ievaditais_vards][uz_valodu]
        else:
            print(f"Šis vārds ir vārdnīcā, bet netiek atrasts {uz_valodu} tulkojums. (LŪDZU PARLIECINĀTIES PAR VĀRDA PAREIZU TŪLKOJUMU)")
            tulkots = GoogleTranslator(source='auto', target=f'{uz_valodu}').translate(ievaditais_vards)
            vardnica[ievaditais_vards][uz_valodu] = tulkots
            return tulkots
    else:
        print("Diemžēl šis vārds nav atrodams vārdnīcā, bet tas tiks iztulkots izmantojot tulkotāju. (LŪDZU PARLIECINĀTIES PAR VĀRDA PAREIZU TŪLKOJUMU)")
        tulkots = GoogleTranslator(source='auto', target=f'{uz_valodu}').translate(ievaditais_vards)
        vardnica[ievaditais_vards] = {uz_valodu: tulkots}
        return tulkots

while True:
    print('Ievadiet tulkojamo vārdu latviešu valodā (beigt lai izietu, vardnica lai apskatītu vārdnīcu): ')
    ievade = input().strip().lower()

    if ievade == 'beigt':
        break
    elif ievade == 'vardnica':
        print('Izvadīt visu vai kādu noteiktu vārdu(suns,kaķis u.c): ')
        var = input().strip().lower()
        if var == 'visi':
            print(vardnica)
        else:
            print(vardnica[f'{var}'])
        continue

    print('Uz kuru valodu tulkot (en, de): ')
    valoda = input().strip().lower()

    iztulkots = tulkojums(ievade, valoda)

    print('Vārda tulkojums ir', iztulkots)

print('Programma beidza darbu!')
