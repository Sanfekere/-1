rindas, kolonas = 3, 4
saraksts = [[None] * kolonas for i in range(rindas)]

burts = 'A'
for rinda in range(rindas):
    for kolona in range(kolonas):
        saraksts[rinda][kolona] = burts
        burts = chr(ord(burts) + 1)

for rinda in saraksts:
    for elements in rinda:
        print(elements, end=' ')
    print()

print()

for rinda in reversed(saraksts):
    for elements in reversed(rinda):
        print(elements, end=' ')
    print()
