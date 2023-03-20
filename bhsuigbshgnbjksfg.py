# ﻿Klases darbs

# Dota programma:
# ====================================
# // Programma ģenerē 2-dimensiu masīva (4 rindām un 5 kolonām) nejaušus skaitļus
# // un izvada tos tabulas/matricas formā

import random

R = 4
K = 5


t = [[random.randint(0, 2) for j in range(K)] for i in range(R)]


for i in range(R):
    for j in range(K):
        print("{:3}".format(t[i][j]), end="")
    print()

print()

new_t = [['O' if t[i][j] == 0 else '-' if t[i][j] == 1 else 'X' for j in range(K)] for i in range(R)]

for i in range(R):
    for j in range(K):
        print("{:3}".format(new_t[i][j]), end="")
    print()

        
# ====================================
# Uzdevums: 
# Izmainīt un papildināt doto programmu lai izpildītos sekojoši nosacījumi. 
# // Programma ģenerē 2-dimensiu masīva (r rindām un k kolonām) nejaušus skaitļus: 0, 1 un 2.
# // (programmas sākumā r un k jādefinē kā konstantes, pieņemot patvaļīgaas vērtības ne lielākas par 20)
# // Izvada skaitļu masīvu tabulas/matricas formā uz ekrāna.
# // No iegūtā masīva jāizveido jauns masīvs, kurā 
# // `0` jāaizstāj ar `O` 
# // `1` jāaizstāj ar `-`
# // `2` jāaizstāj ar `X`
# // un jāizvada uz ekrāna lai būtu redzams sākotnējais un jauniegūtais masīvs.