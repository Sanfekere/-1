# Izveidot 2 dimensiju sarakstu ar X rindām un X kolonnām, kur X ievada lietotājs. 
# Jāņem vērā, ka X nevar būt mazāks par 2 un lielāks par 20. 
# Aizpildīt ar nejaušiem skaitļiem no 0 līdz 9 (ieskaitot). 
# Izvadīt sarakstu tabulas izskatā elementus atdalot ar atstarpi (bez komatiem).

# Izvadīt pirmās kolonas visus elementus vienā rindā atdalot ar atstarpi (bez komata).
# Izvadīt tabulas abu 'diagonāļu' elementu vērtības un to summu!
# Iesniegt risinājumu kā *.py failu.

import random

R = int(input("Ievadi rindu skaitu, bet ne mazāk par 2 un ne lielāku par 20 - "))
K = int(input("Ievadi kolonnu skaitu, bet ne mazāk par 2 un ne lielāku par 20 - "))

if R < 2 or K < 2:
    print("Ievadiet sk ne mazāku par 2!!!")
    if R < 2:
        R = int(input("Ievadi rindu skaitu - "))
    elif K < 2:
        K = int(input("Ievadi kolonnu skaitu - "))
elif R > 20 or K > 20:
    print("Ievadiet sk ne mazāku par 2!!!")
    if R > 20:
        R = int(input("Ievadi rindu skaitu - "))
    elif K > 20:
        K = int(input("Ievadi kolonnu skaitu - "))


t = [[random.randint(0, 9) for j in range(K)] for i in range(R)]

for i in range(R):
    for j in range(K):
        print("{:3}".format(t[i][j]), end="")
    print()

print()
print("Izvadīt pirmās kolonas visus elementus vienā rindā atdalot ar atstarpi (bez komata).")
print()

for i in range(1):
    for j in range(K):
        print("{:3}".format(t[i][j]), end="")
    print()

# b = np.asarray(t)
# print('Diagonal (sum): ', np.trace(b))
# print('Diagonal (elements): ', np.diagonal(b))

g = 0
o = K-1
dio = 0
dio2 = 0
for i in range(R):

    dio += t[i][g]
    dio2 += t[i][o]
    g += 1
    o -= 1

print("1 diognāles summa",dio)
print("2 diognāles summa",dio2) 