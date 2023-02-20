# 1) Programma pieprasa n veselus skaitļus, saglabā tos masīvā un paziņo: vismazāko skaitli un
# tā indeksu (kārtas numuru).
# 2) Pieprasīt masīvu, kas satur N dažādus veselus skaitļus, atrast lielākās un mazākās vērtības
# starpību.
# 3) Sastādīt programmu, kas pieprasa ievadīt 10 skaitļus un paziņo kurš no skaitļiem ir
# mazākais (ievadīto skaitļu vērtības saglabāt masīvā).
# 4) Programma pieprasa n veselus skaitļus, saglabā tos masīvā un paziņo to skaitļu skaitu, kas
# ir mazāki par vidējo aritmētisko.
# 5) Programma pieprasa n veselus skaitļus, saglabā tos masīvā un paziņo, vai masīvā ir skaitlis,
# kas ir vienāds ar visu masīva elementu vidējo aritmētisko.
# 6) Programma pieprasa n veselus skaitļus, saglabā tos masīvā un izveido jaunu masīvu, kas
# satur dotā masīva negatīvos skaitļus.
# 7) Pieprasīt masīvu, kas satur N veselus skaitļus, paziņot, kādu skaitļu tajā vairāk: pāra vai
# nepāra.
# 8) Sastādīt programmu, kas ģenerē nejaušu skaitļu masīvu A, kas satur n elementus.
# Noteikt, vai tajā ir negatīvi elementi. Skaitļu masīvu arī izvadīt uz ekrāna.
# 9) Sastādīt programmu, kas ģenerē nejaušu skaitļu masīvu, kas satur skaitļus diapazonā no –
# 10 līdz +10. Iegūto masīvu izvadīt ekrānā.
# 10) Sastādīt programmu, kas ģenerē nejaušu skaitļu masīvu ar N (ne vairāk par 50) naturāliem
# skaitļiem (ne lielākiem par 1000), saglabā tos masīvā, aprēķina un izvada uz ekrāna:
# a) visus masīva elementus,
# b) visu skaitļu vidējo aritmētisko vērtību,
# c) masīva lielāko skaitli un masīva mazāko skaitli,
# d) pāra un nepāra skaitļu skaitu.
sanja = []
n = int(input("Ievadiet cik skaitļus jūs rakstīsiet"))

for i in range(n):
    sanja.append(int(input("Ievadiet", i , "skaitli: ")))

print(sanja)
