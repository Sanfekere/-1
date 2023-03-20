# ﻿Klases darbs

# Dota programma:
# ====================================
# // Programma ģenerē 2-dimensiu masīva (4 rindām un 5 kolonām) nejaušus skaitļus
# // un izvada tos tabulas/matricas formā

import random

# Define constants for the size of the matrix
R = 4
K = 5

# Generate a matrix of random integers 0, 1, and 2
t = [[random.randint(0, 2) for j in range(K)] for i in range(R)]

# Print the original matrix
print("Original matrix:")
for i in range(R):
    for j in range(K):
        print("{:3}".format(t[i][j]), end="")
    print()

# Create a new matrix by replacing 0 with 'O', 1 with '-', and 2 with 'X'
new_t = [['O' if t[i][j] == 0 else '-' if t[i][j] == 1 else 'X' for j in range(K)] for i in range(R)]

# Print the new matrix
print("\nNew matrix:")
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